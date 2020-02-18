import flask_wtf
import wtforms
from wtforms import validators

class LoginForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name", [validators.Length(min=6, max=8)])
    password = wtforms.PasswordField("Password")
    info = wtforms.StringField("Info", [validators.data_required()])
    submit = wtforms.SubmitField("Submit")