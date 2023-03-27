from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator,MaxValueValidator,MinValueValidator
from datetime import datetime,timezone,timedelta

class Item(models.Model):

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_items')
    buyer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='buyed_items',blank=True,null=True)
    potential_buyer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='first_bider_items',blank=True,null=True)
    second_potential_buyer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='second_bider_items',blank=True,null=True)

    name = models.CharField(db_index=True,max_length=100,unique=True,validators=[MinLengthValidator(10,message='It should be 10+ characters')])


    #slug=models.SlugField(db_index=True,blank=True,null=True,unique=True)
    ItemCondition = models.TextChoices('ItemCondition', 'نو  کارکرده خراب')
    condition= models.CharField(blank=False, choices=ItemCondition.choices, max_length=10)
    description=models.TextField()
    image1=models.ImageField(upload_to=None,height_field=None, width_field=None, max_length=500)
    image2=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=500,blank=True,null=True)
    image3=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=500,blank=True,null=True)


    starting_bid_price=models.IntegerField(validators=[MinValueValidator(1)])
    auction_status=models.BooleanField(default=True)
    buy_it_now_price=models.IntegerField(validators=[MinValueValidator(1)])
    current_highest_bid=models.IntegerField(blank=True,null=True,validators=[MinValueValidator(1)])
    bid_increment=models.IntegerField(blank=True,null=True,validators=[MinValueValidator(1)])

    biding_end_date=models.DateTimeField()
    create_date=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.name}'

    def clean(self):
        if (self.biding_end_date-datetime.now(timezone.utc)).total_seconds()<86400:
            raise ValidationError('The biding end date should be at least one day after item creation!')

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)

        super(Item, self).save(*args, **kwargs)



    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})






