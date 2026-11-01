# INF601 - Advanced Programming in Python
# Your Name
# Mini Project 6

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Book, Genre


class PublicPageTests(TestCase):
    def test_public_pages_load(self):
        for name in ["home", "about", "login", "register"]:
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200, name)

    def test_book_list_requires_login(self):
        response = self.client.get(reverse("book_list"))
        self.assertRedirects(response, reverse("login") + "?next=" + reverse("book_list"))


class AuthTests(TestCase):
    def test_register_logs_user_in(self):
        response = self.client.post(reverse("register"), {
            "username": "reader",
            "email": "reader@example.com",
            "password1": "Sup3rS3cretPass!",
            "password2": "Sup3rS3cretPass!",
        })
        self.assertRedirects(response, reverse("book_list"))
        self.assertTrue(User.objects.filter(username="reader").exists())

    def test_login_and_logout(self):
        User.objects.create_user("reader", password="Sup3rS3cretPass!")
        response = self.client.post(reverse("login"), {"username": "reader", "password": "Sup3rS3cretPass!"})
        self.assertRedirects(response, reverse("book_list"))
        response = self.client.post(reverse("logout"))
        self.assertRedirects(response, reverse("home"))


class BookTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("reader", password="Sup3rS3cretPass!")
        self.other = User.objects.create_user("other", password="Sup3rS3cretPass!")
        self.genre = Genre.objects.create(name="Fantasy")
        self.client.login(username="reader", password="Sup3rS3cretPass!")

    def test_create_edit_delete_book(self):
        response = self.client.post(reverse("book_create"), {
            "title": "The Hobbit", "author": "J.R.R. Tolkien",
            "genre": self.genre.pk, "status": "finished", "rating": 5, "notes": "",
        })
        book = Book.objects.get(title="The Hobbit")
        self.assertEqual(book.owner, self.user)
        self.assertRedirects(response, book.get_absolute_url())

        detail = self.client.get(book.get_absolute_url())
        self.assertContains(detail, "deleteModal")

        self.client.post(reverse("book_update", args=[book.pk]), {
            "title": "The Hobbit", "author": "J.R.R. Tolkien",
            "genre": self.genre.pk, "status": "reading", "rating": "", "notes": "Rereading",
        })
        book.refresh_from_db()
        self.assertEqual(book.status, "reading")

        self.client.post(reverse("book_delete", args=[book.pk]))
        self.assertFalse(Book.objects.filter(pk=book.pk).exists())

    def test_cannot_view_other_users_book(self):
        book = Book.objects.create(title="Secret", author="X", owner=self.other)
        response = self.client.get(book.get_absolute_url())
        self.assertEqual(response.status_code, 404)

    def test_admin_pages_load(self):
        User.objects.create_superuser("boss", password="Sup3rS3cretPass!")
        self.client.login(username="boss", password="Sup3rS3cretPass!")
        Book.objects.create(title="Dune", author="Frank Herbert", genre=self.genre, owner=self.user)
        for url in ["/admin/books/book/", "/admin/books/book/add/", "/admin/books/genre/",
                    f"/admin/books/genre/{self.genre.pk}/change/"]:
            self.assertEqual(self.client.get(url).status_code, 200, url)
