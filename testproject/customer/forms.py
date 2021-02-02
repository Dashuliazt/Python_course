from django.test import TestCase
from django import forms
from .models import *
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

#google recaptcha
from captcha.fields import ReCaptchaField
from captcha.fields import ReCaptchaV2Checkbox

# standart recaptcha
# from captcha.fields import CaptchaField, CaptchaTextInput


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Введите старый пароль'}),
        label='Старый пароль')
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Введите новый пароль'}),
        label='Новый пароль')
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class': 'form-control',
                'placeholder':'Повторите новый пароль'}),
        label='Повторите новый пароль')



class ResetPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                    'placeholder': 'example@example.com'
                   }),
        label='Введите ваш почтовый адрес')
    #google recaptcha
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    #stadart recaptcha
    # captcha = CaptchaField(widget=CaptchaTextInput(
    #     attrs={'class': 'form-control',
    #            'placeholder': 'Докажи что ты не робот'
    #            }
    # ),
    #     label=''
    # )

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                    'placeholder': 'Ваше имя'}),
        label='Имя пользователя')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Пароль'}),
        label='Пароль')

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Ваше имя'}),
        label='Имя пользователя')
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Email'}),
        label='E-mail')
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Пароль'}),
        label='Пароль')
    password2 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class': 'form-control',
                'placeholder':'Подтверждение пароля'}),
        label='Подтверждение пароля')

    class Meta:
        model = User
        fields = {
            'username',
            'email',
            'password1',
            'password2'
        }


# Create your tests here.
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'second_name',
            'birthdate',
            'salary',
            'profession'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthdate': forms.SelectDateWidget(
                attrs={'class': 'form-select mr-3'},
                years=range(1915, datetime.now().year+1)),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'profession': forms.Select(attrs={'class': 'form-select'})
        }



class ProfessionForm(forms.ModelForm):
    profession_name = forms.CharField(max_length=25)

    class Meta:
        model = Professions
        fields = (
            'profession_name',
        )
        widgets = {
            'profession_name': forms.TextInput(attrs={'class': 'form-control'})
        }