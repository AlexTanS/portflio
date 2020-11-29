from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms


# new user registration form
# [rus] форма для регистрации нового пользователя
class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
