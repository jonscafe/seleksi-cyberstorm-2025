from flask import Flask, request, render_template_string
from lxml import etree

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document Validator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 500px;
                width: 90%;
            }
            h1 {
                color: #2c3e50;
            }
            p {
                margin: 10px 0 20px;
                color: #555;
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            label {
                font-weight: bold;
                margin-bottom: 5px;
            }
            input[type="file"] {
                margin-bottom: 20px;
            }
            button {
                background-color: #3498db;
                color: #fff;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #2980b9;
            }
            a {
                text-decoration: none;
                color: #3498db;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Document Validator</h1>
            <p>Upload your XML document to validate its structure and metadata.</p>
            <form method="post" action="/validate" enctype="multipart/form-data">
                <label for="file">Upload XML File:</label>
                <input type="file" name="file" accept=".xml" required>
                <button type="submit">Validate</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/validate', methods=['POST'])
def validate():
    if 'file' not in request.files:
        return "No file uploaded.", 400

    file = request.files['file']
    try:

        xml_data = file.read().decode('utf-8')
        parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
        root = etree.fromstring(xml_data.encode('utf-8'), parser) 

        title = root.find('title').text if root.find('title') is not None else "No title"
        author = root.find('author').text if root.find('author') is not None else "Unknown author"

        return render_template_string(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Validation Results</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .container {{
                    text-align: center;
                    background: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    max-width: 500px;
                    width: 90%;
                }}
                h1 {{
                    color: #2c3e50;
                }}
                p {{
                    margin: 10px 0 20px;
                    color: #555;
                }}
                a {{
                    text-decoration: none;
                    color: #3498db;
                    font-weight: bold;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Validation Results</h1>
                <p>Title: {title}</p>
                <p>Author: {author}</p>
                <a href="/">Back to home</a>
            </div>
        </body>
        </html>
        """)
    except etree.XMLSyntaxError as e:
        return "Invalid XML file. Please ensure it follows the correct structure.", 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10002)
