# Math Mayhem – IPD Prototype (Django)

This is an **interim prototype** for the final-year project: a child-friendly maths game with multiple interactive tasks,
login, saved progress, and a progression bar.

## Requirements
- Python 3.10+
- Django 5.x
- SQLite (included with Python)

## Quick start (Windows / VS Code)
1. Open this folder in VS Code (the folder that contains **manage.py**)
2. Install Django:
   - `pip install django`
3. Run migrations:
   - `python manage.py migrate`
4. Create demo data (tasks + demo user):
   - `python manage.py seed_demo`
5. Start the server:
   - `python manage.py runserver`
6. Open:
   - Home: http://127.0.0.1:8000/tasks/
   - Ribbon Task (Task 10): http://127.0.0.1:8000/ribbon/

## Demo login
- Username: `demochild`
- Password: `demo12345`

## What’s implemented (IPD scope)
- Login (Django auth)
- Home/task list page with a simple progress bar
- Task placeholders for Tasks 1–16
- **Task 10 Ribbon Bows** interactive prototype
- Saves completion + attempts when the user completes Task 10 and clicks “Next Task (12)”

## Notes
- For the IPD, only Task 10 is interactive; other tasks are placeholders.
- Progress/attempts are stored in `db.sqlite3` after migration and usage.

## Deploy on GitHub + Render (no surprises setup)

### 1) Upload to GitHub
1. Create a new GitHub repo.
2. Upload the contents of this folder (the one containing `manage.py`, `requirements.txt`, and `render.yaml`).

### 2) Deploy on Render
**Option A (recommended): Blueprint deploy**
1. On Render: New + → **Blueprint**.
2. Select your GitHub repo. Render will read `render.yaml` and create:
   - a Web Service (Django)
   - a PostgreSQL database

**Option B: Manual service**
- Build command: `bash build.sh`
- Start command: `gunicorn task10_project.wsgi:application`
- Add environment variable: `SECRET_KEY` (random long string)
- Add environment variable: `DEBUG` = `False`
- Add environment variable: `DATABASE_URL` (if you create a Render Postgres DB)

### Notes
- Static files are served using WhiteNoise (`collectstatic` runs in `build.sh`).
- Database automatically switches to Postgres when `DATABASE_URL` is set; otherwise it uses SQLite.
