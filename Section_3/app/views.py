from flask import render_template
from app import app


@app.route('/')

def displayFruit():
    fruits = ["Apple", "Banana", "Orange", "Kiwi"]
    return render_template("fruit_with_inheritance.html", fruits=fruits)
