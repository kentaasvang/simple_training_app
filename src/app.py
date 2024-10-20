from os import getenv
from flask import Flask, render_template_string
from dotenv import load_dotenv

load_dotenv(".env.dev")
STA_BASE_URL = getenv("STA_BASE_URL", "/")

app = Flask(__name__)


@app.route(STA_BASE_URL)
def index():
    return render_template_string("<h1> hello world")
