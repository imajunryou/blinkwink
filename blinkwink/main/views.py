from random import sample

from flask import redirect, render_template, request, url_for
from . import main
from .forms import QuestionForm
from ..reasoning import Category, UniversalAffirmative, \
    UniversalNegative, ParticularAffirmative, ParticularNegative

CATEGORIES = [
    Category("Cats"),
    Category("Dogs"),
    Category("Birds"),
    Category("People"),
    Category("Fish"),
    Category("Lizards"),
    Category("Bugs"),
    Category("Spiders"),
    Category("Invertebrates"),
    Category("Vertebrates"),
    Category("Happy", "Things that are"),
    Category("Angry", "Things that are"),
    Category("Sad", "Things that are"),
    Category("Colorful", "Things that are"),
    Category("Shiny", "Things that are"),
    Category("Fuzzy", "Things that are"),
    Category("Smooth", "Things that are"),
    Category("Sharp", "Things that are"),
    Category("Glowy", "Things that are"),
    Category("Heavy", "Things that are"),
    Category("Exist", "Things that", always_use_prefix=True),
    Category("Eat", "Things that", always_use_prefix=True),
    Category("Sing", "Things that", always_use_prefix=True),
    Category("Jump", "Things that", always_use_prefix=True),
    Category("Make noise", "Things that", always_use_prefix=True)
]

TYPES = [
    UniversalAffirmative,
    UniversalNegative,
    ParticularAffirmative,
    ParticularNegative
]


def kind_of_categorical():
    cat1, cat2 = sample(CATEGORIES, 2)
    statement_type = sample(TYPES, 1)[0]
    return statement_type(cat1, cat2)


@main.route("/")
def index():
    return render_template("index.html")


def build_new_question():
    QUESTIONS = {
        "What kind of categorical statement is this?": kind_of_categorical
    }
    question = sample(list(QUESTIONS.keys()), 1)[0]
    statement = QUESTIONS[question]()
    return question, statement


@main.route("reasoning", methods=["GET", "POST"])
def reasoning():
    form = QuestionForm(request.form)

    if request.method == "POST":
        for opt in form.options:
            if opt.data and "csrf" not in opt.label.text.lower():
                if opt.label.text == form.answer.data:
                    status = "Correct"
                else:
                    status = "Wrong"
                return redirect(
                    url_for('main.reasoning_status', status=status)
                )
    else:
        question, statement = build_new_question()
        form.question.data = question
        form.statement.data = statement
        form.answer.data = statement.kind

    return render_template(
        "reasoning_project.html",
        form=form
    )


@main.route("reasoning/<status>")
def reasoning_status(status):
    return render_template("reasoning_status.html", status=status)


@main.route("econ")
def econ():
    return render_template("econ_project.html")


@main.route("english")
def english():
    return render_template("english.html")

@main.route("stats")
def stats():
    return render_template("stats.html")

@main.route("english_2")
def english_2():
    return render_template("english2.html")

@main.route("english_3")
def english_3():
    return render_template("english3.html")

@main.route("anthropology")
def anthropology():
    return render_template("anthropology.html")

@main.route("calc")
def calc():
    return render_template("calc.html")

@main.route("strength")
def strength():
    return render_template("strength.html")

@main.route("philosophy")
def philosophy():
    return render_template("philosophy.html")

@main.route("macroecon")
def macroecon():
    return render_template("macroecon_project.html")
