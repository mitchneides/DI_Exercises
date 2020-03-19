from django.forms import *


class SignUpForm(Form):
    username = CharField(max_length=60, required=True, widget=TimeInput(
        {'class': 'form-control w-75'}))
    password = CharField(max_length=60, required=True, widget=PasswordInput(
        {'class': 'form-control w-75'}))
    email = EmailField(widget=EmailInput(
        {'class': 'form-control w-75'}))
    first_name = CharField(max_length=60, required=True, widget=TextInput(
        {'class': 'form-control w-75'}))
    last_name = CharField(max_length=60, required=True, widget=TextInput(
        {'class': 'form-control w-75'}))


class LoginForm(Form):
    username = CharField(max_length=60, required=True, widget=TimeInput(
        {'class': 'form-control w-75'}))
    password = CharField(max_length=60, required=True, widget=PasswordInput(
        {'class': 'form-control w-75'}))