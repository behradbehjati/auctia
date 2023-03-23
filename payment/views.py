from django.shortcuts import render
from django.db.models import Q
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Item
from .mixins import PaymentOwnerMixin
from .models import Payment
class MyPaymentView(LoginRequiredMixin,ListView):
    model = Payment
    paginate_by = 10
    context_object_name='payments'
    
    template_name = 'payment/mypayments.html'
    def get_queryset(self):
        queryset=Payment.objects.filter(Q(debtor=self.request.user)|Q(creditor=self.request.user))
        return queryset




