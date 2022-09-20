from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")

@app.get("/about")
def about():
    me = {
        "first_name": "Cory",
        "last_name": "Fonteyne",
        "hobbies": "woodworking",
        "bio": "My name is Cory Fonteyne and I like turtles"
    }
    return render_template("about.html", about_dict=me)

@app.get("/objects")
def objects():
    return render_template("objects.html")