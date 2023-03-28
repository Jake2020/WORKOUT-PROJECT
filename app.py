import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show Home Page"""
    return render_template("index.html")


@app.route("/new_workout", methods=["GET", "POST"])
@login_required
def new_workout():
    """Create New Workout"""
    if request.method == "GET":
        return render_template("new_workout.html")

    if request.method == "POST":
        # Assign workout name
        workout_name = request.form.get("workout_name")

        # Assign reps based on user input
        reps = request.form.get("reps")
        if reps == "strength":
            reps = 6
        else:
            reps = 12

        # Get value for each selection and assign to var
        leg_1 = request.form.get("leg_1")
        leg_2 = request.form.get("leg_2")

        push_1 = request.form.get("push_1")
        push_2 = request.form.get("push_2")

        pull_1 = request.form.get("pull_1")
        pull_2 = request.form.get("pull_2")

        user_id = session["user_id"]
        username = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = username[0]["username"]
        # return apology(f"{username}")

        # Put user selections into database
        # CREATE TABLE workout (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id INTEGER NOT NULL, username TEXT NOT NULL, workout_name TEXT NOT NULL, leg_1 TEXT NOT NULL, leg_2 TEXT NOT NULL, push_1 TEXT NOT NULL, push_2 TEXT NOT NULL, pull_1 TEXT NOT NULL, pull_2 TEXT NOT NULL, reps INTEGER NOT NULL);
        db.execute("INSERT INTO workout (user_id, username, workout_name, leg_1, leg_2, push_1, push_2, pull_1, pull_2, reps) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", user_id, username, workout_name, leg_1, leg_2, push_1, push_2, pull_1, pull_2, reps)

        # Notify user workout successfully created
        flash("Workout Created!")

        return render_template("new_workout.html")


@app.route("/workout", methods=["GET", "POST"])
@login_required
def workout():
    """Start Saved Workout"""
    if request.method == "GET":
        # Get user ID
        user_id = session["user_id"]

        # Gets list of workouts from workout DB
        workouts = db.execute("SELECT * FROM workout")

        # Return workouts page so user can select
        return render_template("workout.html", user_id = user_id, workouts = workouts)

    if request.method == "POST":
        # Get selected workout from form
        workout_id = request.form.get("workout")

        # Get workout info from database
        workout = db.execute("SELECT * FROM workout WHERE id = ?", workout_id)

        # Pass info to template
        return render_template("start_workout.html", workout = workout)

        #return apology(f"{workout}")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # If submitting form
    if request.method == "POST":

        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was provided
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmation was provided and matches
        elif not request.form.get("confirmation"):
            return apology("Confirmation field required", 400)

        elif password != confirmation:
            return apology("Passwords must match", 400)

        # Send to server/database
        else:
            password = generate_password_hash(password)
            username = request.form.get("username")
            exists = db.execute("SELECT username FROM users WHERE username = ?", username)
            # Check user doesn't already exist
            if len(exists) == 1:
                return apology("User already exists")
            else:
                db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password)
                return redirect("/")

    # else just show register page
    else:
        return render_template("register.html")

