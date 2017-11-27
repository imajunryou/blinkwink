from flask import render_template
from . import main

@main.route("/")
def index():
    return render_template("index.html")

@main.route("reasoning")
def reasoning():
    return render_template("reasoning_project.html")
