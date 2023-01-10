from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.form("")

@app.route("/<username>"):
def welcome():
    return "Welcome" + login.username
    