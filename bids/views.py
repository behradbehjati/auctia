from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .redis import get_top10_bidders,current_highest_bid_sync
from items.utils import time_correction
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import NotTheSellerMixin
from market.models import Item


class LiveBidView(LoginRequiredMixin,NotTheSellerMixin,View):

    def get(self,request,pk):
        base_bid = Item.objects.get(id=pk).starting_bid_price
        buy_it_now_price=Item.objects.get(id=pk).buy_it_now_price


        context = {
            'pk':pk,
            'base_bid':base_bid,
            'buy_it_now_price':buy_it_now_price


        }
        return render(request,'bids/livebid.html',context)
class LiveBidChartView(LoginRequiredMixin,View):
    def get(self,request,pk):

        top10=get_top10_bidders(pk)
        current=current_highest_bid_sync(pk)
        highest_bid = current[0][1]  if current!=[] else 0
        print(highest_bid)
        for item in top10:
            item[0]=User.objects.get(id=item[0]).username
            item[2]=time_correction(item[2])
        return JsonResponse({
            'top10':top10,
            'highest':highest_bid,


        })


