# Flui Template — Django 5

A minimal demo application built with **Django 5.2 LTS** + Django REST Framework + drf-spectacular, ready to deploy on [Flui](https://flui.cloud).

Includes:

- Django 5.2 LTS on Python 3.13
- `/health/` endpoint
- In-memory item store with full CRUD on `/items/`
- OpenAPI 3.1 spec auto-generated via drf-spectacular at `/api/openapi/`
- Swagger UI at `/docs/`
- Multi-stage `#flui-managed` Dockerfile
- Gunicorn for production

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

This repo ships with a [`flui.yaml`](./flui.yaml) manifest describing the build strategy, port, healthcheck and resource profile.

From the CLI, with `flui` installed and authenticated against your cluster:

```bash
flui deploy ./flui.yaml
```

The CLI reads the manifest, triggers a build via GitHub Actions and rolls out the workload.

From the UI:

1. Click **Use this template** on GitHub.
2. Connect the new repository to Flui.
3. Click **Deploy**.

Built for [Flui](https://github.com/flui-cloud/flui-core) — see the main repo for cluster setup and CLI installation.

## License

MIT
