### INF601 - Advanced Programming in Python
### Rachel White
### Mini Project 6


# Reading List

A Django web app for keeping track of the books you want to read, are reading, and have finished.

## Description

Reading List is a small Django web app where each user registers an account, logs in, and keeps a private list of books. Every book has a title, author, genre, and reading status (Want to Read, Currently Reading, or Finished), plus an optional 1–5 star rating and personal notes. Users can add, edit, filter, and delete their own books, and they can't see anyone else's list. The site uses Bootstrap 5 for its layout, including a "How does it work?" modal on the home page and a delete-confirmation modal on each book's page. Registration and login are built on Django's authentication system (`UserCreationForm`, `LoginView`, `LogoutView`). Staff users can manage all books and genres through a customized Django admin with list columns, filters, search, fieldsets, and inline editing. The project is one Django project (`mysite`) with one app (`mysite/books`), seven pages that all extend a shared `base.html` template, and a SQLite database.

## Getting Started

### Dependencies

* Python 3.12 or newer (tested with Python 3.13 on the Linux class server and Python 3.14 on Windows 11)
* Git, to download the project
* An internet connection when browsing the site, because Bootstrap loads from a CDN
* The Python packages in `requirements.txt` (Django 6.1.2 and the packages it depends on), installed with:
```
pip install -r requirements.txt
```

### Installing

* Download the project from GitHub:
```
git clone https://github.com/rachelr801/miniproject6RachelWhite.git
cd miniproject6RachelWhite
```
* Create and turn on a virtual environment, then install the requirements:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
On Windows, run `venv\Scripts\activate` instead of `source venv/bin/activate`.
* `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in `mysite/settings.py` are set for the class server `dev-student20.fhsucyber.com`. To run the site on your own computer, add `"localhost"` and `"127.0.0.1"` to `ALLOWED_HOSTS`.
* Project layout:
```
miniproject6RachelWhite/
├── manage.py
├── requirements.txt
├── README.md
├── mysite/                      # Project package (settings, root URLs)
│   ├── settings.py
│   ├── urls.py
│   └── books/                   # The app
│       ├── admin.py             # Admin customization
│       ├── forms.py             # BookForm and RegisterForm
│       ├── models.py            # Genre and Book models
│       ├── tests.py             # Automated tests
│       ├── urls.py              # App URL routes
│       ├── views.py             # Page views
│       ├── migrations/          # Includes the starter genre list
│       └── templates/books/     # home, about, book_list, book_detail, book_form
└── templates/                   # base.html, registration/login.html, registration/register.html
```

### Executing program

* Create migration files from the models. The app already includes its migrations, so this reports "No changes detected" unless you change a model:
```
python manage.py makemigrations
```
* Apply the migrations to build the SQLite database (`db.sqlite3`). This also adds a starter set of genres (Biography, Fantasy, Historical Fiction, Horror, Mystery, Nonfiction, Romance, Science Fiction, Thriller, Young Adult) for the Add Book drop-down:
```
python manage.py migrate
```
* Create an admin account so you can log in at `/admin/`, and follow the prompts for a username, email, and password:
```
python manage.py createsuperuser
```
* Start the development server:
```
python manage.py runserver
```
On the class server, use `python manage.py runserver 0.0.0.0:8000` instead.
* Open the site in a browser (<http://127.0.0.1:8000/> locally, or <https://dev-student20.fhsucyber.com/> on the class server).
* Register a new account (or log in with your superuser), then use **Add Book** to start your list.
* Pages: Home (`/`), About (`/about/`), Register (`/register/`), Log in (`/login/`), My Books (`/books/`), Book detail (`/books/<id>/`), Add/Edit book (`/books/add/`, `/books/<id>/edit/`), and Admin (`/admin/`, staff only).
* Run the automated tests:
```
python manage.py test
```

## Help

* **`DisallowedHost` or "Bad Request (400)":** the address you're using isn't in `ALLOWED_HOSTS` in `mysite/settings.py`. Add it, for example `"localhost"` and `"127.0.0.1"` for local runs.
* **The genre drop-down is empty:** run `python manage.py migrate` to add the starter genres, or add genres in the admin under **Genres**.
* **"That port is already in use":** another server is already running. Stop it before starting a new one:
```
pkill -f "manage.py runserver"
```
* **Keep the site running after closing the SSH tab:**
```
nohup python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &
```
* To list all of Django's management commands:
```
python manage.py help
```

## AI Usage

I used Claude (Anthropic's AI assistant, through Claude Code) to help build this project. I gave it the assignment requirements and the starting Django project, and it:

* suggested the Reading List idea and designed the `Genre` and `Book` models
* wrote the views, forms, URL routes, and admin customization
* wrote the Bootstrap templates, including the two modals
* set up registration and login using Django's built-in auth views
* added a migration that fills in starter genres
* wrote the automated tests and this README
* made the git commits along the way and helped me deploy to the class server

I reviewed the code, ran the app and tests myself, and made sure I understand how each part works.

## Authors

Rachel White
[@rachelr801](https://github.com/rachelr801)

## Version History

* 0.4
    * Starter genres added automatically by `migrate`
    * README rewritten in the class template format
* 0.3
    * Moved the `books` app inside the `mysite` package
    * Set `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for the class server
    * Added name/class/project headers to the Python files
* 0.2
    * Register, login, and logout system
    * Bootstrap templates with modals
    * Automated tests
* 0.1
    * Initial Release: Django project, `books` app, models, and admin
    * See [commit history](https://github.com/rachelr801/miniproject6RachelWhite/commits/main)

## License

This project was created as coursework for INF601 and is not licensed for reuse.

## Acknowledgments

Inspiration, code snippets, etc.
* [Django documentation](https://docs.djangoproject.com/en/6.1/)
* [Django authentication views](https://docs.djangoproject.com/en/6.1/topics/auth/default/#module-django.contrib.auth.views)
* [Bootstrap 5 documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Bootstrap modals](https://getbootstrap.com/docs/5.3/components/modal/)
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
