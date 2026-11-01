"""
Name: Rachel White
Class: Python Programming
Project: Mini Project 6 - Django Reading List

Django admin configuration for the books app.
"""

from django.contrib import admin

from .models import Book, Genre

admin.site.site_header = "Reading List Admin"
admin.site.site_title = "Reading List Admin"
admin.site.index_title = "Manage Books and Genres"


class BookInline(admin.TabularInline):
    """Show a genre's books right on the genre edit page."""

    model = Book
    fields = ("title", "author", "status", "owner")
    extra = 0
    show_change_link = True


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "book_count")
    search_fields = ("name",)
    inlines = [BookInline]

    @admin.display(description="Books")
    def book_count(self, obj):
        return obj.books.count()


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "status", "rating", "owner", "date_added")
    list_filter = ("status", "genre", "rating", "owner")
    list_editable = ("status",)
    search_fields = ("title", "author", "notes")
    date_hierarchy = "date_added"
    autocomplete_fields = ("genre",)
    readonly_fields = ("date_added",)
    fieldsets = (
        ("Book Info", {"fields": ("title", "author", "genre")}),
        ("Reading Progress", {"fields": ("status", "rating", "notes")}),
        ("Ownership", {"fields": ("owner", "date_added")}),
    )
