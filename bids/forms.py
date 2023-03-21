from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class BidForm(forms.Form):
    bid=forms.IntegerField(
        widget=forms.TextInput(
            attrs={'id':'bid-price'}
        )
    )