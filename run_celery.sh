#!/bin/sh

# wait for other redis/rabbit start
sleep 5

export C_FORCE_ROOT="true"
python manage.py migrate --noinput
celery -A shopping_cart worker -l info

# you can docker exec into container and run flower to monitor celery
# celery -A shopping_cart flower