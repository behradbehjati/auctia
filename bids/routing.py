from django.urls import path
from .cosumers import DashboardConsumer
websocket_urlpatterns=[

    path('ws/<pk>/', DashboardConsumer.as_asgi()),

]