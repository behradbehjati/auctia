from celery import shared_task
from market import models
from bids.redis import get_top2_bidders
from django.contrib.auth.models import User
from payment.payment_utils import payment_creation
@shared_task()
def end_bid_date_reached(item_id):
    item=models.Item.objects.get(id=item_id)
    top2=get_top2_bidders(item_id)

    potential_buyer=User.objects.get(id=top2[0][0]) if len(top2)>=1 else None
    price=top2[0][1 ]if len(top2)>=1 else None
    second_potential_buyer=User.objects.get(id=top2[1][0]) if len(top2)==2 else None

    if second_potential_buyer:
        item.potential_buyer=potential_buyer
        item.second_potential_buyer=second_potential_buyer
        print('you had two bidders')
        payment_creation(item,potential_buyer,item.seller,price)
    elif potential_buyer and not second_potential_buyer:
        item.potential_buyer=potential_buyer
        payment_creation(item, potential_buyer, item.seller, price)
        print('you had one bidder')

    else:
        print('you had no bid')

    item.auction_status=False
    item.save()

