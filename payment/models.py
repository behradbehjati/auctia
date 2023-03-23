from django.db import models
from market.models import Item
from django.contrib.auth.models import User
from datetime import datetime,timedelta,timezone
class Payment(models.Model):
    item=models.OneToOneField(Item, on_delete=models.CASCADE)
    debtor=models.ForeignKey(User,on_delete=models.CASCADE,related_name="owed_payments")
    creditor=models.ForeignKey(User,on_delete=models.CASCADE,related_name="demand_payments")
    expire_time=models.DateTimeField()
    price=models.IntegerField()
    reminder=models.DateTimeField()
    paid=models.BooleanField(default=False)
    payment_date=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return f'{self.id}'

    def save(self,*args,**kwargs):
        self.expire_time=datetime.now(timezone.utc)+timedelta(days=4)
        self.reminder=datetime.now(timezone.utc)+timedelta(days=2)
        super(Payment, self).save(*args, **kwargs)







