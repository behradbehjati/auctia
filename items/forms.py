from django import forms
from django.forms import ModelForm
from market.models import Item

class CreateItemForm(ModelForm):
    class Meta:
        CREATEITEM={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'condition':forms.Select(attrs={'class': 'form-select'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
            'starting_bid_price':forms.TextInput(attrs={'class': 'form-control'}),
            'buy_it_now_price':forms.TextInput(attrs={'class': 'form-control'}),
            'biding_end_date':forms.DateInput(attrs={'type': 'date','id': 'datepicker'})

        }
        model=Item
        exclude=('seller','buyer','potential_buyer','second_potential_buyer','current_highest_bid','payment_information','shipping_information','auction_status')
        widgets=CREATEITEM
