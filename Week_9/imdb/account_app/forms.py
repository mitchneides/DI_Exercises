from django.forms import *


# from django.contrib.auth.forms import UserCreationForm
#     ^Django has a pre-made template, but here we will make our own:


class SignUpForm(Form):
    username = CharField(max_length=60, required=True, widget=TimeInput())
    password = CharField(max_length=60, required=True, widget=PasswordInput())
    email = EmailField(widget=EmailInput())
    first_name = CharField(max_length=60, required=True, widget=TextInput())
    last_name = CharField(max_length=60, required=True, widget=TextInput())


class LoginForm(Form):
    username = CharField(max_length=60, required=True, widget=TimeInput())
    password = CharField(max_length=60, required=True, widget=PasswordInput())
