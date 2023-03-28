#!/bin/bash

python manage.py collectstatic --noinput
python manage.py compilemessages 
gunicorn main.wsgi:application --bind 0.0.0.0:8000
