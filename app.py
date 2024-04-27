import os
from flask import Flask

app = Flask(__name__)

# Set background color to purple and text color to white
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to docker Tarik!</title>
    <style>
        body {
            background-color: purple;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        .chat-button {
            position: absolute;
            left: 200px;
            top: 150px;
            background-color: lightblue;
            color: black;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <a href="/howareyou" class="chat-button">How are you?</a>
    <h1>Welcome to docker Tarik!</h1>
</body>
</html>
"""

@app.route("/")
def main():
    return html_template

@app.route('/howareyou')
def hello():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>How are you?</title>
    <style>
        body {
            background-color: grey;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
    </style>
</head>
<body>
    <h1>How are you?</h1>
    <p>I am good, how about you?</p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run()