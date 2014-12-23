from flask import Flask, render_template, session
from app.models import session as db_session
from app import app, db


@app.route('/')
def index():
    return "Hello, World!"

