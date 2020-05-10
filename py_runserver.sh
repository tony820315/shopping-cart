#!/bin/sh

# wait for other redis/rabbit start
sleep 5

python manage.py migrate --noinput
python /code/manage.py runserver 0.0.0.0:8000