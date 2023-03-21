from django.urls import path
from . import views
app_name='items'
urlpatterns=[
    path('create/',views.CreateItemView.as_view(),name='createitemview'),
    path('update/<pk>/',views.UpdateItemView.as_view(),name='updateitemview'),
    path('detail/<pk>/',views.DetailItemView.as_view(),name='detailitemview'),

]
