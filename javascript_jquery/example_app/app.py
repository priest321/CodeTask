from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask import request


app = Flask(__name__)
app.config["SECRET_KEY"] = "ABCD"


@app.route("/")
def hello():
    return "hello world"
    

@app.route("/greet/<name>")
def greet(name):
    return render_template("index.html", message=f"hello, {name}!")

@app.route("/table")
def table():
    return render_template("hello.html")



if __name__ == "__main__":
    app.run(debug=True)