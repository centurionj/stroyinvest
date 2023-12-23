#!/bin/bash

python "/app/manage.py" migrate

python "/app/manage.py" collectstatic --noinput

gunicorn "stroyinvest.wsgi:application" --bind 0.0.0.0:8000 &

celery -A "stroyinvest" worker -l info &

nginx -g 'daemon off;'