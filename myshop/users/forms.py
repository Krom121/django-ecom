from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

"""
Below is the form class that has been mainly create by the user creation form.
which comes built into django. This where i have add a email field, as
the user creation field only comes with username and password when
first rendered to template.

"""
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']