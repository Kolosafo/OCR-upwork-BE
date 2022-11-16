#!/bin/sh
set -e

python manage.py runserver
echo "done"
echo "$@"
exec "$@"