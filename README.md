# Mini Project 6 – Reading List (Django)

**Name:** Rachel White
**Class:** Python Programming
**Project:** Mini Project 6 – Django Web App

## About the Project

Reading List is a small Django web app for keeping track of books. Each user registers an account, logs in, and keeps a private list of books they want to read, are currently reading, or have finished. Books can be given a genre, a 1–5 star rating, and personal notes.

### Features

- **Register / login / logout** using Django's built-in authentication (`UserCreationForm`, `LoginView`, `LogoutView`).
- **Add, edit, and delete books** through a Bootstrap-styled form. Users can only see and change their own books.
- **Filter** your list by status (Want to Read, Currently Reading, Finished).
- **Bootstrap 5** layout with a responsive navbar, cards, alerts, and two **modals**:
  - a "How does it work?" modal on the home page
  - a delete-confirmation modal on each book's detail page
- **Django admin** customized for both models: list columns, filters, search, inline editing of status, fieldsets on the edit page, a date drill-down, and genre pages that show their books inline.

### Pages

| Page | URL | Login required |
|------|-----|----------------|
| Home | `/` | No |
| About | `/about/` | No |
| Register | `/register/` | No |
| Log in | `/login/` | No |
| My Books (list) | `/books/` | Yes |
| Book detail (with delete modal) | `/books/<id>/` | Yes |
| Add book (form) | `/books/add/` | Yes |
| Edit book (form) | `/books/<id>/edit/` | Yes |
| Admin | `/admin/` | Staff only |

## Folder Structure

```
miniproject6RachelWhite/
├── manage.py
├── requirements.txt
├── README.md
├── mysite/                      # Project package
│   ├── settings.py
│   ├── urls.py                  # Root URLs (admin, login, logout, app)
│   ├── asgi.py
│   ├── wsgi.py
│   └── books/                   # The app (inside the mysite package)
│       ├── admin.py             # Admin customization
│       ├── apps.py              # App config (name = "mysite.books")
│       ├── forms.py             # BookForm and RegisterForm
│       ├── models.py            # Genre and Book models
│       ├── tests.py             # Automated tests
│       ├── urls.py              # App URL routes
│       ├── views.py             # Page views
│       ├── migrations/
│       └── templates/books/     # App page templates
│           ├── home.html
│           ├── about.html
│           ├── book_list.html
│           ├── book_detail.html
│           └── book_form.html
└── templates/                   # Project-wide templates
    ├── base.html                # Bootstrap layout every page extends
    └── registration/
        ├── login.html
        └── register.html
```

## Installation

You need Python 3.12 or newer.

1. Clone the repository and move into it:

   ```bash
   git clone <repository-url>
   cd miniproject6RachelWhite
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```

   macOS / Linux:

   ```bash
   source venv/bin/activate
   ```

3. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

## Database Initialization

The project uses SQLite, so there is no database server to set up. The `db.sqlite3` file is created automatically.

1. Create migration files from the models (the app already includes its migration, so this should report "No changes detected" unless you change a model):

   ```bash
   python manage.py makemigrations
   ```

2. Apply the migrations to build the database tables:

   ```bash
   python manage.py migrate
   ```

3. Create an admin (superuser) account so you can log in to `/admin/`:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts for a username, email, and password.

4. `migrate` also adds a starter set of **Genres** (Biography, Fantasy, Historical Fiction, Horror, Mystery, Nonfiction, Romance, Science Fiction, Thriller, Young Adult), so the genre drop-down on the Add Book form is ready to use. To add, rename, or remove genres, log in at `/admin/` and open **Genres**.

## Running the Development Server

```bash
python manage.py runserver
```

Then open <http://127.0.0.1:8000/> in your browser. Register a new account (or log in with your superuser) and start adding books. Press `Ctrl+C` in the terminal to stop the server.

`ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in `mysite/settings.py` are set for the class dev server `dev-student20.fhsucyber.com`. To run the site on your own computer instead, add `"localhost"` and `"127.0.0.1"` to `ALLOWED_HOSTS`.

## Running the Tests

```bash
python manage.py test
```

The tests check that the public pages load, that registration and login work, that a user can add, edit, and delete a book, that users can't see each other's books, and that the admin pages load.

## AI Usage

I used Claude (Anthropic's AI assistant, through Claude Code) to help build this project. I gave it the assignment requirements and the starting Django project, and it:

- suggested the Reading List idea and designed the `Genre` and `Book` models
- wrote the views, forms, URL routes, and admin customization
- wrote the Bootstrap templates, including the two modals
- set up registration and login using Django's built-in auth views
- wrote the automated tests and this README
- made the git commits along the way

I reviewed the code, ran the app and tests myself, and made sure I understand how each part works.
