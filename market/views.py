from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Item
class MarketPlaceView(ListView):
    model = Item
    paginate_by = 10
    context_object_name='public_items'
    ordering='-create_date'
    template_name = 'market/marketplace.html'


