from django.urls import path
from . import views
app_name='accounts'
urlpatterns=[
    path('',views.DashboardView.as_view(),name='dashboardview'),
    path('register/',views.RegisterView.as_view(),name='registerview'),
    path('login/',views.LoginView.as_view(),name='loginview'),
    path('logout/',views.LogoutView,name='logoutview'),

]