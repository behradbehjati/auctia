from django import forms
from django.forms import ModelForm
from market.models import Item

class CreateItemForm(ModelForm):
    class Meta:
        CREATEITEM={
            'biding_end_date':forms.DateInput(attrs={'type': 'date','class': 'datepicker'})

        }
        model=Item
        exclude=('seller','buyer','current_highest_bid','payment_information','shipping_information',)
        widgets=CREATEITEM
