from django.shortcuts import render
from django.views import View
import redis
from django.conf import settings
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,db=1)
class NotificationView(View):
    def get(self,request):
        notifications=redis_client.smembers(f"user:{request.user.id}:notifications")
        notifications_strings = [elem.decode('utf-8') for elem in notifications]
        print(notifications_strings)
        context={"notifications":notifications_strings}
        redis_client.delete(f"user:{request.user.id}:notifications")
        return render(request,"notification/mynotificationsview.html",context)
