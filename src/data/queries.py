from .db_connection import get_connection
from .entities import User, Workout


def select_all_users():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return [User(*user) for user in users]


def select_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users AS user WHERE user.user_id = ?;", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return User(*user)


def insert_new_workout(workout):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO workouts (workout_id, user_id, name, description) 
        VALUES (?, ?, ?, ?)
                            """, (workout.workout_id, workout.user_id, workout.name, workout.description))
    
    connection.commit()
    cursor.close()


def select_all_workouts_by_user_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM workouts as workout WHERE workout.user_id = ?", (user_id,))
    workouts = cursor.fetchall()
    cursor.close()
    return [Workout(*workout) for workout in workouts]


def select_workout_by_workout_id(workout_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM workouts AS workout WHERE workout.workout_id = ?;", (workout_id,))
    workout = cursor.fetchone()
    cursor.close()
    return Workout(*workout)
