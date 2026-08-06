from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": (
                    "block w-full rounded-md bg-white px-3 py-2 "
                    "text-gray-900 outline-1 outline-gray-300 "
                    "focus:outline-2 focus:outline-yellow-500"
                ),
                "placeholder": "Username",
                "autocomplete": "username",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": (
                    "block w-full rounded-md bg-white px-3 py-2 "
                    "text-gray-900 outline-1 outline-gray-300 "
                    "focus:outline-2 focus:outline-yellow-500"
                ),
                "placeholder": "Password",
                "autocomplete": "current-password",
            }
        ),
    )
