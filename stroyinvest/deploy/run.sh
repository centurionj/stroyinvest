#!/bin/bash

python "/app/manage.py" migrate

python "/app/manage.py" collectstatic --noinput

python "/app/manage.py" loaddata "service/fixtures/icons_fixture.json"

gunicorn -c "./deploy/gunicorn.conf.py" stroyinvest.wsgi:application