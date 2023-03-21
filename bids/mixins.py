from market.models import Item
from django.shortcuts import redirect
from django.contrib import messages
class NotTheSellerMixin:

        def dispatch(self, request, *args, **kwargs):
            pk = self.kwargs.get('pk')
            seller=Item.objects.get(id=pk).seller
            if seller==request.user:
                messages.error(request,'صاحب کالا نمی تواند در مزایده شرکت کند')
                return redirect('items:detailitemview' ,pk)


            return super().dispatch(request, *args, **kwargs)


