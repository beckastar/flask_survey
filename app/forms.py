from flask.ext.wtf import Form
from wtforms import TextField, StringField, BooleanField, RadioField, IntegerField, validators
from wtforms.validators import DataRequired, Email, Length

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class PersonForm(Form):
    name    = TextField('Username', [validators.Length(min=4, max=25)])
    email  = TextField('Email Address', [validators.Length(min=6, max=35)])
    age = IntegerField('User Level', [validators.NumberRange(min=0, max=80)])
