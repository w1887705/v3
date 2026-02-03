## Project Overview 
This prototype was built to demonstrate an end-to-end flow: 
- A user can log in with the demo credentials
- Demo tasks are available immediately (seeded into database)
- The prototype is deployable on Render with a Postgres database


## Key Features
- User authentication
- Demo Data seeding (Tasks + demo user)
- Ribbon Task Route
- Render Deployment Support (Postgres + static collection)


## Tech Stack 
- **Backend** : Django
- **Database** : SQLite (for locally) Render Postgres (hosting)
- **Server** : Gunicorn
- **Hosting** : Render

Project Structure Debrief 
task10_project/ - Django project settings and roots URLS
core/ - core apps (tasks, authentication integration, seed commands) 
            - management/commands/seed_demo.py - demo data seeding
ribbongame/ - Ribbon task module
template/ - HTML templates
static/ - static assets
build.sh - render build script
start.sh render startup script (start Gunicorn + migrate/seed)

DEMO LOGIN DETAILS 
Username: demochild 
Password: demo12345

Production
- build.sh --> installs dependencies & collects static files
- start.sh --> runs migrate & seed_demo

Issues encountered & How they were fixed 

1) Demo credentials not working on Render

   Symptom: Site loaded correctly, unable to log in using demo login credentials

   Cause: seed_demo not reliably happening against the Postgres database. Running migrate/seed_demo during build phase ended up seeding the wrong database. (build/runtime differs)

   Fix!!: Moving seeding to start.sh


2) Safe reseeding on redeploy

   Symptom: Seeding fails by duplication

   Fix: Too many seed_demo commands, had to get rid of a lot 
