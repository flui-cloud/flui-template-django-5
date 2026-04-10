# Flui Template — Django 5

A minimal demo application built with **Django 5.2 LTS** + Django REST Framework + drf-spectacular, ready to deploy on [Flui](https://flui.cloud).

This template includes:

- 🐍 Django 5.2 LTS with Python 3.13
- 🩺 `/health/` endpoint
- 📦 In-memory item store with full CRUD (`/items/`)
- 📖 OpenAPI 3.1 spec auto-generated via drf-spectacular (`/api/openapi/`)
- 📚 Swagger UI at `/docs/`
- 🐳 Multi-stage Dockerfile (`#flui-managed`)
- 🏃 Gunicorn for production

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

App runs on http://localhost:8000

## Build with Docker

```bash
docker build -t flui-demo-django .
docker run -p 8000:8000 flui-demo-django
```

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `Flui Demo Django` | App name |
| `APP_VERSION` | `1.0.0` | App version |
| `SECRET_KEY` | `dev-only-...` | Django secret key (CHANGE IN PROD) |
| `DEBUG` | `False` | Django debug mode |
| `PORT` | `8000` | HTTP port |

## Deploy with Flui

1. Click **Use this template** on GitHub
2. Connect to Flui
3. Click **Deploy**

## License

MIT
