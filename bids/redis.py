import time

import redis,time
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime,timezone
import json
from channels.db import database_sync_to_async


# Create a Redis client
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,db=settings.REDIS_DB)





@database_sync_to_async
def add_bid(amount, user_id, item_id):
    # Add a new bid to the Redis sorted set for the item

    redis_client.zadd(f'bidders:{item_id}', {user_id: amount})
    redis_client.zadd(f'amount:{item_id}', {user_id: time.time()})







def get_top10_bidders(item_id ):
    # Get the top bidders for the item from the Redis sorted set
    bidders = redis_client.zrevrange(f'bidders:{item_id}', 0,9, withscores=True)
    x=[[int(user_id), amount] for user_id, amount in bidders]
    for i in x:
            i.append(redis_client.zscore(f'amount:{item_id}', i[0]))



    return x
@database_sync_to_async
def current_highest_bid(item_id):
    highest_bider=redis_client.zrevrange(f'bidders:{item_id}', 0,0, withscores=True)
    print(highest_bider)
    return highest_bider
def current_highest_bid_sync(item_id):
    highest_bider=redis_client.zrevrange(f'bidders:{item_id}', 0,0, withscores=True)
    print(highest_bider)
    return highest_bider
def get_top2_bidders(item_id):
    top2_bidders = redis_client.zrevrange(f'bidders:{item_id}', 0, 1, withscores=True)
    return top2_bidders

