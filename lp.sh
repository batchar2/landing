#!/usr/bin/env bash

cd /service

echo yes | ./lp/manage.py collectstatic

gunicorn \
    --worker-class=gevent\
    --timeout 600 \
    --worker-connections=1000 \
    --workers=4 \
    --threads=4 \
    --log-level=info \
    --bind=0.0.0.0:8000  \
    lp.wsgi:application
