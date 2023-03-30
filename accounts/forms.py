from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import  ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': _('نام کاربری خود را وارد کنید'),'class':'form-control'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': _('رمز عبور خود را وارد کنید'),'class':'form-control'}
        )
    )
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': _('نام کاربری خود را وارد کنید'), 'class': 'form-control'}
        )
    )
    password1= forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': _('رمز عبور خود را وارد کنید'), 'class': 'form-control'}
        )
    )
    password2= forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': _('رمز عبور خود رامجددا وارد کنید'), 'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': _('ایمیل خود را وارد کنید'), 'class': 'form-control'}
        )
    )
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

