#!/bin/sh
set -e

/usr/local/bin/gunicorn ocr_backend.wsgi:application --preload --bind 0.0.0.0:8000 --workers=4 -t 300
echo "done"
echo "$@"
exec "$@"