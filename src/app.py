from os import getenv
from uuid import uuid4
from .data.queries import (
    select_all_users, 
    select_all_workouts_by_user_id, 
    select_user_by_id, 
    insert_new_workout,
    select_workout_by_workout_id
)

from .data.entities import Workout
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv(".env.dev")
STA_BASE_URL = getenv("STA_BASE_URL", "/")

app = Flask(__name__)


@app.route(STA_BASE_URL)
def index():
    users = select_all_users() 
    return render_template("index.html", users=users)


@app.route(f"{STA_BASE_URL}/<user_id>")
def dashboard(user_id):
    user = select_user_by_id(user_id)
    return render_template("dashboard.html", user=user)


@app.route(f"{STA_BASE_URL}/start_workout/<user_id>")
def start_workout(user_id):
    user = select_user_by_id(user_id)
    return render_template("start_workout.html", user=user)


@app.route(f"{STA_BASE_URL}/create_workout/<user_id>", methods=["GET", "POST"])
def create_workout(user_id):
    user = select_user_by_id(user_id)

    if (request.method == "POST"):
        name = request.form["name"]
        description = request.form["description"]
        workout_id = str(uuid4())
        workout = Workout(workout_id=workout_id, user_id=user_id, name=name, description=description)
        insert_new_workout(workout)

        return redirect(url_for("workouts", user_id=user_id))

    return render_template("create_workout.html", user=user)


@app.route(f"{STA_BASE_URL}/workouts/<user_id>")
def workouts(user_id):
    user = select_user_by_id(user_id)
    workouts = select_all_workouts_by_user_id(user_id)
    return render_template("workouts.html", user=user, workouts=workouts)


@app.route(f"{STA_BASE_URL}/workout/<workout_id>/<user_id>")
def workout(workout_id, user_id):
    user = select_user_by_id(user_id)
    workout = select_workout_by_workout_id(workout_id)
    return render_template("workout.html", user=user, workout=workout)
