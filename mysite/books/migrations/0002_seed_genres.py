# INF601 - Advanced Programming in Python
# Rachel White
# Mini Project 6

# Data migration: fills the Genre table with a starter set so the genre
# drop-down on the Add Book form isn't empty on a fresh database.

from django.db import migrations

GENRES = [
    "Biography",
    "Fantasy",
    "Historical Fiction",
    "Horror",
    "Mystery",
    "Nonfiction",
    "Romance",
    "Science Fiction",
    "Thriller",
    "Young Adult",
]


def add_genres(apps, schema_editor):
    Genre = apps.get_model("books", "Genre")
    for name in GENRES:
        Genre.objects.get_or_create(name=name)


def remove_genres(apps, schema_editor):
    Genre = apps.get_model("books", "Genre")
    Genre.objects.filter(name__in=GENRES, books__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_genres, remove_genres),
    ]
