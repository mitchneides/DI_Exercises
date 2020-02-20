import flask_wtf
import wtforms
from wtforms import validators


class Sign_In_Form(flask_wtf.FlaskForm):
    email = wtforms.StringField("Email", [validators.Length(min=4, max=40)])
    password = wtforms.PasswordField("Password", [validators.data_required()])
    submit = wtforms.SubmitField("Sign-in")




