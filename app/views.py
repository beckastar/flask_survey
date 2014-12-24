from flask import Flask, render_template, session, flash, redirect, url_for, request, g
# from app.models import session as db_session
from app import app, db, lm, oid
from .forms import LoginForm
from wtforms.validators import DataRequired
from .models import User, Crash_Incident
from flask.ext.login import login_user, logout_user, current_user, login_required

# from flask.ext.bootstrap3 import Bootstrap
# from flask.ext.login import LoginManager, login_required, logout_user, login_user, current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user


@app.route('/index')
@login_required
def index_login():
    user = g.user
    return render_template('index.html',
                           title='Home',
                           user=user)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faq')
def show_faq():
    return render_template('faq.html')

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

