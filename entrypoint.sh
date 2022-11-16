#!/bin/sh
set -e
RUN_PORT=${PORT:-8000}

/usr/local/bin/gunicorn --worker-tmp-dir /dev/shm -b 127.0.0.1:8000 ocr_backend.wsgi:application

echo "done"
echo "$@"
exec "$@"