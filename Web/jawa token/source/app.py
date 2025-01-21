from flask import Flask, jsonify, request, render_template_string, make_response
import jwt

app = Flask(__name__)

SECRET_KEY = 'fafc6f4ca2b5c8f5b7d4c0f6c6e5f4f4sde4ffea2b5c8f5b7d4c0f6c6e5f4f4sde4ffea'
FLAG = "STORM{JWT_Basic_Dec0ding_00ffed88facc}"

@app.route("/")
def home():
    token = jwt.encode({"flag": FLAG}, SECRET_KEY, algorithm="HS256")
    
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>jawaaaaaaaaaaaaaaaaaa</title>
    </head>
    <body>
        <h1>Raja Jawa</h1>
        <p>jawaaaaaaaaaaaaaaaaaaaaaaaa</p>
        <img src="https://static.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/p2/230/2024/09/22/RAJA-AJWA-677970050.jpg" 
             alt="Challenge Image" 
             style="max-width: 100%; height: auto;">
    </body>
    </html>
    """
    
    response = make_response(render_template_string(html_template))
    response.set_cookie("jwt_token", token, httponly=True, secure=False) 
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10004)
