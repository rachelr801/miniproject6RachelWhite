# INF601 - Advanced Programming in Python
# Your Name
# Mini Project 6

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import BookForm, RegisterForm
from .models import Book


def home(request):
    """Landing page with a few quick stats for logged-in users."""
    context = {}
    if request.user.is_authenticated:
        books = Book.objects.filter(owner=request.user)
        context = {
            "total": books.count(),
            "reading": books.filter(status=Book.Status.READING).count(),
            "finished": books.filter(status=Book.Status.FINISHED).count(),
            "recent": books[:3],
        }
    return render(request, "books/home.html", context)


def about(request):
    """Static page describing the project."""
    return render(request, "books/about.html")


@login_required
def book_list(request):
    """Show the current user's books, optionally filtered by status."""
    books = Book.objects.filter(owner=request.user).select_related("genre")
    status = request.GET.get("status", "")
    if status in Book.Status.values:
        books = books.filter(status=status)
    return render(
        request,
        "books/book_list.html",
        {"books": books, "statuses": Book.Status.choices, "current_status": status},
    )


@login_required
def book_detail(request, pk):
    """Show one book. Users can only see their own books."""
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    return render(request, "books/book_detail.html", {"book": book})


@login_required
def book_create(request):
    """Add a new book using BookForm."""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            messages.success(request, f'"{book.title}" was added to your list.')
            return redirect(book)
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form, "title": "Add a Book"})


@login_required
def book_update(request, pk):
    """Edit an existing book."""
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{book.title}" was updated.')
            return redirect(book)
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form, "title": "Edit Book"})


@login_required
@require_POST
def book_delete(request, pk):
    """Delete a book. Triggered from the confirmation modal on the detail page."""
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    book.delete()
    messages.success(request, f'"{book.title}" was removed from your list.')
    return redirect("book_list")


def register(request):
    """Create a new user account and log them in."""
    if request.user.is_authenticated:
        return redirect("book_list")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account was created.")
            return redirect("book_list")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
