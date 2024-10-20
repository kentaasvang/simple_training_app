
CREATE TABLE users (
    user_id TEXT PRIMARY KEY NOT NULL,
    username TEXT NOT NULL
);


CREATE TABLE exercises (
    exercise_id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    description TEXT
);


CREATE TABLE workouts (
    workout_id TEXT PRIMARY KEY NOT NULL,
    user_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,

    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE exercises_to_workouts (
    exercise_to_workout_id TEXT PRIMARY KEY NOT NULL,
    exercise_id TEXT NOT NULL,
    workout_id TEXT NOT NULL,

    FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id),
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
);


CREATE TABLE exercise_details (
    exercise_detail_id TEXT PRIMARY KEY NOT NULL,
    exercise_to_workout_id TEXT NOT NULL,
    reps INTEGER NOT NULL,
    sets INTEGER NOT NULL,
    weight REAL NOT NULL,

    FOREIGN KEY (exercise_to_workout_id) REFERENCES exercises_to_workouts(exercise_to_workout_id)
);


CREATE TABLE sessions (
    session_id TEXT PRIMARY KEY NOT NULL,
    workout_id TEXT NOT NULL,
    date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL, 

    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
);

