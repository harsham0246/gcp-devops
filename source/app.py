from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello All, welcome to the Home Page"
