from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

from .model import User


def password_validator(password):
    """
    password registration rules
    Now it's an error if  it's less than 8 characters
    for example, if a space is entered, it is jadged not to have been entered
    """
    if len(password) < 8:
        raise ValidationError(
            gettext("パスワードは8文字以上20文字以内で入力してください。"),
            code="invalid password",
        )


class LoginForm(forms.Form):
    """
    define the format of the login page
    default login is by username, so to allow login by userid
    the format is has been changed
    this page is almost a copy of the default form authenticationForm
    """

    userid = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={"autocomplate": True, "placeholder": "UserId"}),
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplate": "curent-password", "placeholder": "Password"}
        ),
    )

    error_massage = {
        "invalid_login": "ユーザーIDかパスワードに誤りがあります",
        "inactive": "アクセス権限がありません",
    }


def __init__(self, request=None, *args, **kwargs):
    self.request = request
    self.user_cache = None
    super().__init__(*args, **kwargs)
