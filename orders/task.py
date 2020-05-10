from django.core.mail import send_mail
from django.conf import settings

from .models import Order
# from celery import task
from shopping_cart.celery import app

@app.task(name = 'task_send_mail')
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order num. {order.id}'
    message = f'Hi {order.first_name},\n\n' \
              f'You have successfully booked an order.' \
              f'Your order ID is {order.id}.' \
              f'We will send your package, usually about two to three working days to receive the parcel.'

    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [order.email])
    return mail_sent