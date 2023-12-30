#!/bin/bash

python "/app/manage.py" migrate

python "/app/manage.py" collectstatic --noinput

python "/app/manage.py" loaddata "service/fixtures/icons_fixture.json"

gunicorn -c "./deploy/gunicorn.conf.py" stroyinvest.wsgi:application &

celery -A "stroyinvest" beat -l info &

celery -A "stroyinvest" worker -l info &

nginx -g 'daemon off;'