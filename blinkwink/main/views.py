from flask import render_template, request
from . import main


@main.route("/")
def index():
    return render_template("index.html")


@main.route("reasoning", methods=["GET", "POST"])
def reasoning():

    return render_template(
        "reasoning_project.html",
        form=request.form
    )


@main.route("econ")
def econ():
    return render_template("econ_project.html")
