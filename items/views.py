from market.models import Item
from .forms import CreateItemForm
from django.views.generic.edit import FormView
from django.views.generic import UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from .mixins import ItemOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404,render
from bids.redis import current_highest_bid_sync,get_top2_bidders
from django.contrib.auth.models import User
from .tasks import end_bid_date_reached
from datetime import datetime,timedelta
from bids.redis import get_top2_bidders




class CreateItemView(LoginRequiredMixin,FormView):
    form_class = CreateItemForm
    template_name = 'items/createitem.html'
    success_url = reverse_lazy('accounts:dashboardview')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        form.save()
        eta = form.cleaned_data['biding_end_date']
        end_bid_date_reached.apply_async([form.instance.id], eta=eta)
        messages.success(self.request, 'Your item has been added successfully')
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors')
        return super().form_invalid(form)
class UpdateItemView(LoginRequiredMixin,ItemOwnerMixin,UpdateView):
    model = Item
    fields= ('name', 'description', 'image1', 'image2', 'image3')
    template_name = 'items/updateitem.html'

    def get_success_url(self):
        if self.object.pk:
            return reverse('items:detailitemview', kwargs={'pk': self.object.pk})

class DetailItemView(View):

    def get(self,request,pk):

        item=get_object_or_404(Item,pk=pk)



        end_date=item.biding_end_date

        top2=get_top2_bidders(pk)
        print(top2)

        highest_bid=current_highest_bid_sync(pk)
        highest_price=highest_bid[0][1] if highest_bid else 0
        highest_bider=User.objects.get(id=highest_bid[0][0]) if highest_bid else 0
        buy_it_now_price=Item.objects.get(id=pk).buy_it_now_price
        context={

            'item':item,
            'highest_price':highest_price,
            'highest_bider':highest_bider,
            'end_date':end_date,
            'buy_it_now_price':buy_it_now_price,



        }
        return render(request,'items/detailitem.html',context)

















