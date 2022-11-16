#!/bin/bash

RUN_PORT=${PORT:-8000}
# gunicorn --worker-tmp-dir /dev/shm ocr_backend.wsgi

/usr/local/bin/gunicorn --worker-tmp-dir /dev/shm -k python manage.py runserver --bind  "0.0.0.0:${RUN_PORT}"