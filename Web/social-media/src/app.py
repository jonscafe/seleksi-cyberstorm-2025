from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
import sqlite3
import hashlib
from datetime import datetime
import time
import pytz

app = Flask(__name__)
app.secret_key = 'REDACTED'
bcrypt = Bcrypt(app)

def init_db():
    conn = sqlite3.connect('social_media.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            writer TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def generate_post_id(post_id, timestamp):
    return hashlib.md5(f"{post_id}{timestamp}".encode()).hexdigest()

# Routes
@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login') 

    username = session['username']
    conn = sqlite3.connect('social_media.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, writer, content, timestamp FROM posts WHERE writer = ?', (username,))
    posts = cursor.fetchall()
    conn.close()

    postIds = [
        (post[0], post[1], post[2], post[3], post[4], 
         hashlib.md5(f"{post[0]}{post[4]}".encode()).hexdigest(),
         datetime.fromtimestamp(int(post[4])).strftime('%Y-%m-%d %H:%M:%S'))  
        for post in posts
    ]

    return render_template('index.html', posts=postIds)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if 'username' not in session:
        return redirect('/login')  

    if request.method == 'POST':
        name = request.form['name']
        content = request.form['content']
        timestamp = str(int(time.time()))

        conn = sqlite3.connect('social_media.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO posts (name, writer, content, timestamp) VALUES (?, ?, ?, ?)', 
                       (name, session['username'], content, timestamp))
        conn.commit()
        conn.close()

        flash('Post created successfully!', 'success')
        return redirect('/')

    return render_template('create_post.html')

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    if 'username' not in session:
        return redirect('/login') 

    conn = sqlite3.connect('social_media.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, writer, content, timestamp FROM posts WHERE id = ?', (post_id,))
    post = cursor.fetchone()

    if not post:
        return "Post not found", 404

    if post[2] != session['username']:  
        flash('You can only edit your own posts', 'error')
        return redirect('/')

    if request.method == 'POST':
        name = request.form['name']
        content = request.form['content']
        timestamp = str(int(time.time()))  
        cursor.execute('UPDATE posts SET name = ?, content = ?, timestamp = ? WHERE id = ?', 
                       (name, content, timestamp, post_id))
        conn.commit()
        conn.close()

        flash('Post updated successfully!', 'success')
        return redirect('/')

    conn.close()
    return render_template('edit_post.html', post=post)

@app.template_filter('datetimeformat')
def datetimeformat(value):
    if value:
        utc_time = datetime.utcfromtimestamp(int(value))
        gmt7 = pytz.timezone('Asia/Bangkok')
        utc_time = pytz.utc.localize(utc_time).astimezone(gmt7)
        return utc_time.strftime('%Y-%m-%d %H:%M:%S')
    return value

@app.route('/profile/<username>')
def view_profile(username):
    if 'username' not in session:
        return redirect('/login')

    conn = sqlite3.connect('social_media.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, timestamp FROM posts WHERE writer = ?', (username,))
    posts = cursor.fetchall()
    conn.close()

    posts_summary = [
        (post[0], post[1], post[2])  
        for post in posts
    ]

    return render_template('user_profile.html', posts=posts_summary, username=username)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        conn = sqlite3.connect('social_media.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        conn.close()

        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect('/register')

        conn = sqlite3.connect('social_media.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()

        flash('Registration successful! You can now log in.', 'success')
        return redirect('/login')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('social_media.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[1], password):
            session['user_id'] = user[0]
            session['username'] = username
            return redirect('/')
        else:
            flash('invalid credential', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()  
    flash('You have been logged out', 'info')  
    return redirect('/login') 

@app.route('/post/<post_id>')
def view_post(post_id):
    if 'username' not in session:
        return redirect('/login')
    conn = sqlite3.connect('social_media.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, writer, content, timestamp FROM posts')
    posts = cursor.fetchall()

    for post in posts:
        if generate_post_id(post[0], post[4]) == post_id:
            conn.close()
            return render_template('post.html', post=post)

    conn.close()
    return "Post not found", 404

@app.before_first_request
def insert_admin_post():
    conn = sqlite3.connect('social_media.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts WHERE writer = "admin"')
    admin_post = cursor.fetchone()
    if not admin_post:
        timestamp = str(int(time.time()))
        cursor.execute('INSERT INTO posts (name, writer, content, timestamp, user_id) VALUES (?, ?, ?, ?, ?)', 
                       ('test', 'admin', 'test deploy', timestamp, 1))  
        conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=False, host='0.0.0.0', port=10003)
