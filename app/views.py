from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User



@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


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
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# @lm.user_loader
# def load_user(id):
# 	return User.query.get(int(id))

# @app.route('/survey_1/', methods=['GET','POST'])
# # @login_required
# def survey_1():
# 	g.user = current_user
# 	if g.user.s1 is False:
# 		form = Survey1Form(request.form)
# 		if form.validate_on_submit():

# 			g.user.s1=True
# 			g.user.lastSeen=date.today()
# 			model = Survey1(gender=form.gender.data, age=form.age.data,
# 				education=form.education.data, language=form.language.data, userid=g.user.userid)

# 			form.populate_obj(model)

# 			db.session.add(model)
# 			db.session.add(g.user)

# 			db.session.commit()
# 			logout_user()

# 			return redirect(url_for('logouthtml'))

# 		return render_template('survey/Survey1.html', title='Survey', form=form)
# 	else:
# 		return redirect(url_for('index'))

# @app.route('/survey_2/', methods=['GET','POST'])
# @login_required
# def survey_2():
# 	g.user = current_user
# 	if g.user.s1 is not False and g.user.s2 is False:
# 		form = Survey2Form(request.form)
# 		if form.validate_on_submit():

# 			g.user.s2=True
# 			g.user.lastSeen=date.today()
# 			model=Survey2(major=form.major.data,
# 				count=form.count.data, unique=form.unique.data, userid=g.user.userid)

# 			form.populate_obj(model)

# 			db.session.add(model)
# 			db.session.add(g.user)

# 			db.session.commit()
# 			logout_user()

# 			return redirect(url_for('logouthtml'))

# 		return render_template('survey/Survey2.html', title='Survey', form=form)
# 	else:
# 		return redirect(url_for('index'))

