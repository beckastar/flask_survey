from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User


@app.route('/index')
def show_homepage():
    return render_template('index.html')

@app.route('/faq')
def show_faq():
    return render_template('faq.html')

@app.route('/survey', methods=['POST'])
def show_survey():
    form = survey_form
    if form.validate_on_submit():
        new_incident = Crash_Incident(crash_incident = form.)
        db.session.add()
        db.session.commit()
    return render_template('survey.html')