#!./venv/bin/python3.12
from src.app import app

if __name__ == "__main__":

    config = {
        "debug": True,
        "host": "127.0.0.1",
        "port": 5001
    }

    app.run(**config)
