from wtforms import Form, fields,  validators, ValidationError
from wtforms import widgets, StringField, BooleanField, RadioField
from wtforms.validators import DataRequired, Email, Length, Regexp
from models import User


def validate_login(form, field):
    user = form.get_user()

    if user is None:
        raise validators.ValidationError('Invalid user')

    if user.password != form.password.data:
        raise validators.ValidationError('Invalid password')

class LoginForm(Form):
    email = fields.TextField(validators=[DataRequired(), Email()])
    password = fields.PasswordField(validators=[DataRequired(), validate_login])

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()

class ForgotPasswordForm(Form):
    email = fields.TextField(validators=[DataRequired(), Email()])

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()

class RegistrationForm(Form):
    email = fields.TextField('Email Address', validators=[DataRequired(), Email(), Regexp('[^@]+@[^@]+[fsu]+\.[edu]+')])
    consent = fields.BooleanField(validators=[DataRequired()])
    password = fields.PasswordField('New Password', [
        validators.DataRequired(), validators.Length(min=8, max=20),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = fields.PasswordField(validators=[DataRequired()])

    def validate_email(self, field):
        if db.session.query(User).filter_by(email=self.email.data).count() > 0:
            raise validators.ValidationError('Duplicate email')

class NewPass(Form):
    password = fields.PasswordField('New Password', [
        validators.DataRequired(), validators.Length(min=8, max=20),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = fields.PasswordField(validators=[DataRequired()])

    def validate_password(self, field):
        if db.session.query(User).filter_by(password=self.password.data).count() > 0:   #NOT SURE IF CORRECT
            raise validators.ValidationError('Duplicate Password')

class Survey1Form(Form):
   injury = fields.RadioField('How badly were you hurt?', choices=[('0','Minor scrapes or bruises'), ('1', 'More severely'), ('2', 'Hospitalized or incapacitated'), ('3', 'This was a fatal crash')], validators = [DataRequired()], default=None)
   age = fields.RadioField('What is your age?', choices=[('lt18', 'Younger than 18'), ('18-24', '18 to 24'), ('25-34', '25 to 34'),
        ('35-44', '35 to 44'), ('45-54', '45 to 54'), ('55', '55 years or older')], validators=[DataRequired()])


class Survey2Form(Form):
    age = fields.RadioField('What is your age?', choices=[('lt18', 'Younger than 18'), ('18-24', '18 to 24'), ('25-34', '25 to 34'),
        ('35-44', '35 to 44'), ('45-54', '45 to 54'), ('55', '55 years or older')], validators=[DataRequired()])