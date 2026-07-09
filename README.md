# Nightshow

Nightshow — a Django web application (project package: `Nightshow`).

A full-stack Django project with template-driven pages, REST API endpoints, social login, OTP support, phone number validation, Paytm payment integration, and QR-code/image handling.

## Key features

- Django 5.x web application and Django REST Framework for APIs
- Social authentication (social-auth-app-django)
- One-time-password / two-factor support (django-otp)
- Phone number handling (django-phonenumber-field + phonenumbers)
- Paytm payment integration (paytmchecksum)
- QR code generation and image support (qrcode, Pillow)
- PostgreSQL-ready (psycopg2-binary)

## Repository layout (inferred)

Nightshow/
- manage.py — Django management script
- requirements.txt — pinned Python dependencies (see Nightshow/requirements.txt)
- Nightshow/ — Django project package
  - __init__.py
  - asgi.py
  - settings.py
  - urls.py
  - wsgi.py
- templates/ — HTML templates
- static/ — static assets (CSS, JS)
- media/ — uploaded media files
- library/ — application code / reusable modules (inspect this folder for apps)
- .idea/ — IDE config (can be ignored)

## Requirements

- Python 3.11+ recommended
- See `Nightshow/requirements.txt` for pinned dependencies (Django, DRF, social-auth, psycopg2, etc.)

## Environment variables (recommended)

Set these in your environment or via a `.env` file (do not commit secrets):

- SECRET_KEY — Django secret key
- DEBUG — `True` or `False`
- ALLOWED_HOSTS — comma-separated hosts
- DATABASE_URL or: DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
- SOCIAL_AUTH_<PROVIDER>_KEY and SOCIAL_AUTH_<PROVIDER>_SECRET — social auth credentials
- PAYTM_MERCHANT_KEY, PAYTM_MID — Paytm credentials
- EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD — email sending
- STORAGE credentials if using S3 for media/static

## Local development

1. Create and activate a virtual environment

   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .\.venv\Scripts\activate  # Windows (PowerShell)

2. Install dependencies

   pip install -r Nightshow/requirements.txt

3. Set required environment variables (at minimum: SECRET_KEY, DEBUG, DATABASE settings).

4. Apply database migrations

   python manage.py migrate

5. Create a superuser

   python manage.py createsuperuser

6. Run the development server

   python manage.py runserver

7. Visit http://127.0.0.1:8000/

## Running in production (simple)

- Use a production-ready database such as PostgreSQL and set `DEBUG=False`.
- Collect static files:

  python manage.py collectstatic

- Run with Gunicorn behind a reverse proxy (NGINX):

  gunicorn Nightshow.wsgi:application --bind 0.0.0.0:8000

- Configure NGINX to serve static files and proxy to Gunicorn. Use TLS at the proxy.

## Recommended improvements

- Add a Dockerfile and docker-compose.yml for local development parity.
- Add CI (GitHub Actions) to run tests, linters, and check migrations.
- Create `.env.example` listing required environment variables.
- Move media serving to object storage (S3) and use a CDN for static assets in production.
- Add Celery + Redis if you need background jobs (email, asynchronous payment verification).
- Add Sentry or similar for error monitoring and structured logging.

## Project-specific files to inspect next

- `Nightshow/settings.py` — confirm INSTALLED_APPS, auth backends, database & static/media settings
- `Nightshow/urls.py` — top-level routes and included app urls
- `library/` — app code (models, views, serializers)
- `templates/` and `static/` — UI templates and assets

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Open a pull request with a descriptive title and summary

## License

Add your preferred license file (e.g., `LICENSE`) to the repository if you want to make licensing explicit.

---

If you want, I can:
- Expand this into a longer README with environment variable details and example `.env` file.
- Add a Dockerfile and docker-compose.yml and commit them.
- Create a `.env.example` with placeholder variable names.
