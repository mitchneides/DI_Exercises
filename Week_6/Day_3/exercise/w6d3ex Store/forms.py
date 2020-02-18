import flask_wtf
import wtforms
from wtforms import validators


class LoginForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name", [validators.Length(min=4, max=20)])
    password = wtforms.PasswordField("Password", [validators.data_required()])
    submit = wtforms.SubmitField("Submit")




