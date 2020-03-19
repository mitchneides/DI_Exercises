from django.forms import *


# from django.contrib.auth.forms import UserCreationForm
#     ^Django has a pre-made template, but here we will make our own:


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
