from django.urls import path
from . import views
app_name="payment"
urlpatterns=[
path('mypayments/',views.MyPaymentView.as_view(),name='mypaymentsview')



]