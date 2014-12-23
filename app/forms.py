from flask import Flask, render_template
from wtforms import Form, fields,  validators, ValidationError, TextField, IntegerField
# from wtforms import widgets, StringField, BooleanField, RadioField
# from wtforms.validators import DataRequired, Email, Length, Regexp

class UserForm(Form):
    cyclist_name    = TextField('Username', [validators.Length(min=4, max=25)])
    cyclist_email  = TextField('Email Address', [validators.Length(min=6, max=35)])
    cyclist_age = IntegerField('User Level', [validators.NumberRange(min=0, max=80)])


class IncidentReportForm(Form):
    name = TextField("Name")
    email = TextField ("Email address")
    injury = fields.RadioField('How badly were you hurt?', choices=[('0','Minor scrapes or bruises'), ('1', 'More severely'), ('2', 'Hospitalized or incapacitated'), ('3', 'This was a fatal crash')], validators = [DataRequired()], default=None)
    age = fields.RadioField('What is your age?', choices=[('lt18', 'Younger than 18'), ('18-24', '18 to 24'), ('25-34', '25 to 34'),
    ('35-44', '35 to 44'), ('45-54', '45 to 54'), ('55', '55 years or older')], validators=[DataRequired()])
