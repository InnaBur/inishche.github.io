import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@app.route("/login")
def login():

    return render_template("login.html")


@app.route("/first", methods=["GET", "POST"])
def first():

    if request.method == "POST":
        if not request.form.get("username"):
            return redirect("/first")
        name = request.form.get("username")

        return render_template("first.html", name=name)
    return redirect("/first")

@app.route("/second", methods=["GET", "POST"])
def second():
    if request.method == "POST":
        animal = request.form.get("animal")
        if animal == "білка" or "Білка" or "БІЛКА":
            flash('Correct')
        else:
            flash('Not Correct')
    return render_template("second.html")


@app.route("/third", methods=["GET", "POST"])
def third():
    if request.method == "POST":
        number = request.form.get("dam")
        if not request.form.get("dam"):
            return render_template("third.html")
        if number == 2:
            return redirect(url_for("/four"))
        else:
            return redirect(url_for("/third"))
    return render_template("third.html")

@app.route("/four", methods=["GET", "POST"])
def four():
    if request.method == "POST":
        build = request.form.get("prom")
        if not request.form.get("prom"):
            return render_template("four.html")
        if build == "бібліотека":
            return redirect(url_for("/five"))
        else:
            return redirect(url_for("/four"))
    return render_template("four.html")

@app.route("/five", methods=["GET", "POST"])
def five():
    if request.method == "POST":
        number_1 = request.form.get("par")
        if not request.form.get("par"):
            return render_template("five.html")
        if number_1 == "17485" or "9П-17485":
            return redirect(url_for("/six"))
        else:
            return redirect(url_for("/five"))
    return render_template("five.html")

@app.route("/six", methods=["GET", "POST"])
def six():
    if request.method == "POST":
        helyc = request.form.get("hely")
        if not request.form.get("hely"):
            return render_template("six.html")
        if helyc == "Ігор":
            return redirect(url_for("/seven"))
        else:
            return redirect(url_for("/six"))
    return render_template("six.html")

@app.route("/seven", methods=["GET", "POST"])
def seven():
    if request.method == "POST":
        return render_template("seven.html")
    return render_template("fin.html")

@app.route("/fin", methods=["GET", "POST"])
def fin():
    if request.method == "POST":
        return render_template("fin.html")