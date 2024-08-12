from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/<name>")
def helloo(name):
    return f"Hello, {escape(name)}!"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)