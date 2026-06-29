# fixers
Django-based home services marketplace connecting customers with verified providers
## Features
- Dual authentication (Customer / Provider roles)
- Multi-step registration flow
- Service request system
- AJAX-powered real-time UI updates

## Tech Stack
- Django 4.x
- SQLite (development)
- Vanilla JS (Fetch API)

## Setup
1. Clone the repo
2. Create `.env` file (see `.env.example`)
3. `pip install -r requirements.txt`
4. `py manage.py migrate`
5. `py manage.py runserver`
