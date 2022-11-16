#!/bin/sh
set -e
RUN_PORT=${PORT:-8000}

/usr/local/bin/gunicorn --worker-tmp-dir /dev/shm -k ocr_backend.wsgi:application --bind "0.0.0.0:${RUN_PORT}"

echo "done"
echo "$@"
exec "$@"