from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from . import models


class RegistrationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ["username", "last_name", "first_name", "password1", "password2",]

