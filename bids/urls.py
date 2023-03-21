from django.urls import path
from . import views
app_name='bids'
urlpatterns=[
    path('<pk>/', views.LiveBidView.as_view(), name='livebidview'),
    path('<pk>/chart/', views.LiveBidChartView.as_view(), name='livebidchartview'),


]