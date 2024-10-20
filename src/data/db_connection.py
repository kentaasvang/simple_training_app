import sqlite3

DB_CONNECTION_STRING = "sta.db"


def _get_connection():
    connection = sqlite3.connect(DB_CONNECTION_STRING)
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection


def get_connection():
    connection = _get_connection()
    return connection


