import redis
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime,timezone
from celery import shared_task
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,db=1)
@shared_task()
def notif_creation_task(user_id,notif_message):
    set_key = f"user:{user_id}:notifications"
    redis_client.sadd(set_key, notif_message)

