from django.forms import *
from .models import *


# class LoginForm(Form):
#     username = CharField(max_length=60, required=True, widget=TimeInput(
#         {'class': 'form-control w-75'}))
#     password = CharField(max_length=60, required=True, widget=PasswordInput(
#         {'class': 'form-control w-75'}))
#
#
# class ProfileModelForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['picture', 'bio']
#         widgets = {
#             'bio': Textarea(attrs={'class': 'form-control'}),
#             'picture': FileInput(attrs={'class': 'form-control'}),
#         }