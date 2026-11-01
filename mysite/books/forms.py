"""
Name: Rachel White
Class: Python Programming
Project: Mini Project 6 - Django Reading List

Forms for adding books and registering new users.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Book


class BookForm(forms.ModelForm):
    """Form used to add or edit a book on the reading list."""

    class Meta:
        model = Book
        fields = ["title", "author", "genre", "status", "rating", "notes"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "genre": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 5}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


class RegisterForm(UserCreationForm):
    """Sign-up form: Django's UserCreationForm plus an email field."""

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Give every field Bootstrap styling.
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
