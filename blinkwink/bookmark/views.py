from flask import redirect, render_template, request, url_for
from . import bookmark

@bookmark.route("/")
def bm_index():
    return render_template("bm_index.html")