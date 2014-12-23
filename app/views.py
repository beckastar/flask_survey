from flask import Flask, render_template, session
from app.models import session as db_session
from app import app, db
from .models import User, Crash_Incident

# from flask.ext.bootstrap3 import Bootstrap
# from flask.ext.login import LoginManager, login_required, logout_user, login_user, current_user


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# @app.route('/faq')
# def show_faq():
#     return render_template('faq.html')

@app.route('/user_survey', methods=['POST'])
def show_survey():
    cyclist_name = request.form["cyclist_name"]
    cyclist_email = request.form["cyclist_email"]
    cyclist_age = request.form["cyclist_age"]
    user = models.User(cyclist_name = cyclist_name, cyclist_email=cyclist_email, cyclist_age=cyclist_age)
    models.session.add(user)
    db.session.add(user)
    db.session.commit()
    return render_template('survey.html')

