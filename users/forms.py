from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    field_order = ['username', 'password1', 'password2']
