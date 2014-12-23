from flask import Flask, render_template, session
from app.models import session as db_session
from app import app, db

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)