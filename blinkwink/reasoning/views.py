from flask import render_template
from . import reasoning

@reasoning.route("/")
def reasoning():
    return render_template("reasoning_project.html")
