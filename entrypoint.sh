#!/bin/bash

RUN_PORT=${PORT:-8000}
# gunicorn --worker-tmp-dir /dev/shm ocr_backend.wsgi

python manage.py runserver --noinput || exit 1