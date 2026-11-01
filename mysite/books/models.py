"""
Name: Rachel White
Class: Python Programming
Project: Mini Project 6 - Django Reading List

Database models for the books app.
"""

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """A category a book can belong to (Fantasy, Mystery, etc.)."""

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    """A book on a user's reading list."""

    class Status(models.TextChoices):
        WANT_TO_READ = "want", "Want to Read"
        READING = "reading", "Currently Reading"
        FINISHED = "finished", "Finished"

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, blank=True, related_name="books"
    )
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.WANT_TO_READ
    )
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate from 1 to 5 stars (optional).",
    )
    notes = models.TextField(blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="books"
    )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.pk])

    def stars(self):
        """Return the rating as a string of star characters for templates."""
        if not self.rating:
            return ""
        return "★" * self.rating + "☆" * (5 - self.rating)
