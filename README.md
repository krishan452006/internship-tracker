# Internship Tracker

A Django-based web application that helps students organize and track internship applications in one place.

## Features

* Student registration and login
* Add, edit, and delete internship applications
* Track application statuses
* Search and filter applications
* Dashboard statistics for applications, interviews, and selections
* Student profiles with resume uploads
* Upcoming interview tracking

## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS
* **Database:** SQLite for local development
* **Deployment:** Render (planned)

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/krishan452006/internship-tracker.git
   cd internship-tracker
   ```

2. Create and activate a virtual environment.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser.

## Status

Under development.
