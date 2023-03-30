from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views import View
from .forms import LoginForm
from django.core.exceptions import ValidationError
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from market.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from notification.notifs_tasks import notif_creation_task
from .forms import RegisterForm


class LoginView(View):

    form_class=LoginForm
    def get(self,request):
        form=self.form_class()
        context = {
            'form': form
        }
        return render(request,'profile/login.html',context)
    def post(self,request):
        redirect_to = False
        if 'next' in request.GET:
         redirect_to = request.GET['next']
         print(redirect_to)

        form=self.form_class(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            data=form.cleaned_data
            username=User.objects.filter(username=data['username']).exists()
            if username:

                user=authenticate(username=data['username'],password=data['password'])
                if user is not None:
                    login(request,user)
                    if redirect_to:
                        return redirect(redirect_to)
                    return redirect('accounts:dashboardview')

        messages.error(request,_('The username or password is incorrect'))
        return render(request,'profile/login.html',context)
@login_required
def LogoutView(request):
    logout(request)
    return redirect(reverse_lazy('market:marketplaceview'))


class RegisterView(CreateView):
    model = User
    form_class=RegisterForm
    template_name = 'profile/register.html'
    success_url = reverse_lazy('market:marketplaceview')
    def form_valid(self, form):
        valid=super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        notif_creation_task.delay(self.request.user.id, f'کاربر گرامی به آکتیا خوش آمدید')
        return valid



class DashboardView(LoginRequiredMixin,View):

    def get(self,request):

        name=request.user.username
        items=Item.objects.filter(seller=request.user)
        context={
            'items':items,
            'name':name,
        }
        return render(request,'profile/dashboard.html',context)


