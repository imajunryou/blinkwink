from flask import render_template, request
from . import main
from .forms import WhichTransformUsedForm


@main.route("/")
def index():
    return render_template("index.html")


@main.route("reasoning", methods=["GET", "POST"])
def reasoning():
    options = ["First", "Second", "Third"]
    if request.method == "POST":
        form = WhichTransformUsedForm(request.form)
        try:
            options.remove(form.answer.data)
        except ValueError:
            pass

    return render_template(
        "reasoning_project.html",
        form=WhichTransformUsedForm(request.form),
        remaining_options=options
    )


@main.route("econ")
def econ():
    return render_template("econ_project.html")
