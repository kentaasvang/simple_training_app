
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


class Exercise:
    def __init__(self, exercise_id, name, description):
        self.exercise_id = exercise_id
        self.name = name
        self.description = description


class Workout:
    def __init__(self, workout_id, user_id, name, description):
        self.workout_id = workout_id
        self.user_id = user_id
        self.name = name
        self.description = description


class ExerciseToWorkout:
    def __init__(self, exercise_to_workout_id, exercise_id, workout_id):
        self.exercise_to_workout_id = exercise_to_workout_id
        self.exercise_id = exercise_id
        self.workout_id = workout_id


class ExerciseDetail:
    def __init__(self, exercise_detail_id, exercise_to_workout_id, reps, sets, weight):
        self.exercise_detail_id = exercise_detail_id
        self.exercise_to_workout_id = exercise_to_workout_id
        self.reps = reps
        self.sets = sets
        self.weight = weight


class Session:
    def __init__(self, session_id, workout_id, date):
        self.session_id = session_id
        self.workout_id = workout_id
        self.date = date
