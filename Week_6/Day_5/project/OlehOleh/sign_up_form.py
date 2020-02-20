import flask_wtf
import wtforms
from wtforms import validators


class Sign_Up_Form(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name", [validators.Length(min=4, max=30)])
    email = wtforms.StringField("Email", [validators.Length(min=4, max=40)])
    password = wtforms.PasswordField("Password", [validators.data_required()])
    submit = wtforms.SubmitField("Sign-up")




