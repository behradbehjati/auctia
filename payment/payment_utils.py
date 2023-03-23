from .models import Payment
from market.models import Item
from django.contrib.auth.models import User
def payment_creation(item,debtor,creditor,price):
    Payment.objects.create(item=item,debtor=debtor,creditor=creditor,price=price)
    print('payment created')