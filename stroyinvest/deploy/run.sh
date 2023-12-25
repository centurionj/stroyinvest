#!/bin/bash

python "/app/manage.py" migrate

python "/app/manage.py" collectstatic --noinput

python "/app/manage.py" loaddata "service/fixtures/icons_fixture.json"

gunicorn "stroyinvest.wsgi:application" --bind 0.0.0.0:8000 &

celery -A "stroyinvest" beat -l info &

celery -A "stroyinvest" worker -l info &

nginx -g 'daemon off;'