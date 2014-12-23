from flask import Flask, render_template
from wtforms import Form, fields,  validators, ValidationError, TextField, IntegerField
# from wtforms import widgets, StringField, BooleanField, RadioField
# from wtforms.validators import DataRequired, Email, Length, Regexp

class PersonForm(Form):
    name    = TextField('Username', [validators.Length(min=4, max=25)])
    email  = TextField('Email Address', [validators.Length(min=6, max=35)])
    age = IntegerField('User Level', [validators.NumberRange(min=0, max=80)])
