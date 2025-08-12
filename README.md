# Django Web Application with Authentication

A clean and professional Django-based web application providing user registration, login/logout, and profile management with modern user interface and secure authentication.

---

## Features

- **User Registration:** New users can sign up with username, email, and passwords.
- **User Login & Logout:** Secure login with password visibility toggle and logout option.
- **User Profile:** Personalized profile page with welcome message and logout button.
- **Password Visibility Toggle:** Eye icons to show/hide passwords on sign-in and sign-up forms.
- **Success Toasts:** Friendly messages after successful actions like account creation.
- **Responsive & Modern UI:** Warm beige themed, mobile-friendly styling.
- **Django Admin Access:** Superusers can log in at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to manage site content, users, permissions, and more.

---

## Tools & Technologies

- **Django** – Python web framework for backend and templating.
- **SQLite** – Default lightweight database for development.
- **HTML/CSS/JavaScript** – Frontend UI design and interactivity.
- **Django Authentication Forms** – For user login and registration.
- **Google Fonts (Montserrat)** – Clean typography.

---

## Project Structure

```
Django-Web-Application-with-Authentication/
├── assets/
│   └── demo.mp4
├── blog/                                      # Main app containing your app's code
│   ├── __init__.py                            # Marks this as a Python package
│   ├── admin.py                               # Django admin model registrations
│   ├── apps.py                                # App configuration
│   ├── forms.py                               # Custom Django forms
│   ├── models.py                              # Database models for the app
│   ├── urls.py                                # URL routes for this app
│   ├── views.py                               # Request/response logic
│   ├── templates/                             # HTML templates for this app
│   │   └── blog/
│   │       ├── base.html                      # Base template for extending
│   │       ├── login.html                     # Login page template
│   │       ├── password_reset.html            # Password reset form
│   │       ├── password_reset_complete.html   # After successful reset
│   │       ├── password_reset_confirm.html    # Link > enter new password
│   │       ├── password_reset_done.html       # Email sent confirmation
│   │       ├── profile.html                   # User profile page
│   │       └── register.html                  # Sign-up page template
│   └── migrations/
│       └── __init__.py                        # Marks this as a Python package
├── env                                        # Python virtual environment folder
├── migrations/                                # Extra migrations folder (if used manually)
│   └── __init__.py
├── myblog/                                    # Django project settings and config
│   ├── __init__.py
│   ├── asgi.py                                # ASGI server entrypoint
│   ├── settings.py                            # Project settings
│   ├── urls.py                                # Main URL routing
│   └── wsgi.py                                # WSGI server entrypoint
├── static/                                    # Development static files
│   ├── eye.svg                                # Open-eye icon for password toggle
│   ├── eye-slash.svg                          # Closed-eye icon for password toggle
│   └── style.css                              # Custom site styles
├── staticfiles/                               # Collected static files for production
│   ├── admin/                                 # Django admin interface static assets
│   │   ├── css/                               # CSS files for Django admin style
│   │   ├── img/                               # Images/icons used by Django admin
│   │   └── js/                                # JavaScript files for Django admin UI
│   └── style.css                              # Your collected CSS from /static
├── db.sqlite3                                 # SQLite database (created after migrate)
├── manage.py                                  # Django CLI management tool
├── requirements.txt
├── .gitignore
├── README.md
└── Report.pdf
```

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <GitHub repository link>
   cd <project folder>
   ```
   > _Replace `<GitHub repository link>` with the actual URL of this repository, and `<project folder>` with the folder name._

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (for admin access):**
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts for username, email, and password.

5. **Run the development server:**
   ```
   python manage.py runserver
   ```
   Then visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the user sign in page.

---

## How to Remove Old User Data

1. **Stop server if running** (CTRL+C in old terminal first)

2. **Delete old database** (optional if you want a clean start)
    ```
    del db.sqlite3
    ```

3. **Delete all migration files except __init__.py**

    ```
    Get-ChildItem -Path .\blog\migrations\ -Filter *.py -Recurse | Where-Object { $_.Name -ne '__init__.py' } | Remove-Item -Force
    ```

4. **Clear all Python cache files**

    ```
    Get-ChildItem -Path . -Filter *.pyc -Recurse | Remove-Item -Force
    Get-ChildItem -Path . -Directory -Recurse | Where-Object { $_.Name -eq '__pycache__' } | Remove-Item -Recurse -Force
    ```
    
---

## Future Enhancements

- Integration with email verification for signup.
- Role-based access controls.
- Advanced user analytics and dashboard.
- Deployment-ready configuration for cloud hosting.

---