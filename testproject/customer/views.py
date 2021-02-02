import random
import string
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View, ListView, CreateView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import *
from .mixins import *
from .forms import *


class ChangePassword(View):


    def get(self, request):
        form = ChangePasswordForm(request.user)
        return render(request, 'customer/change_password.html', {'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.user, data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Пароль успешно изменён!')
            return redirect('auth')
        messages.error(request, 'Ошибка изменения пароля!')
        return render(request, 'customer/change_password.html', {'form': form})





class ResetPassword(View):

    def get(self, request):
        form = ResetPasswordForm()
        return render(request, 'customer/reset_password.html', {'form':form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)

        if form.is_valid():
            symbols = string.ascii_letters + string.digits + string.punctuation
            new_passwd = ''.join(random.sample(symbols, 10))
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
                user.set_password(new_passwd)
                user.save()
                send_mail('Сброс пароля', f'{user.username}, '
                                          f'Ваш новый пароль {new_passwd}. '
                                          f'После успешной авторизации, '
                                          f'рекомеендуем сменить пароль.',
                          'djangotest@ukr.net',[user.email], fail_silently=True)
                messages.success(request, f'Сообщение с новым паролем отправлено '
                                          f'на {user.email}')
                return redirect('auth')
            except User.DoesNotExist:
                messages.error(
                    request,
                    f'Пользователь с таким email не зарегистрирован!')
                return render(request, 'customer/reset_password.html',
                              {'form': form})




class RegistrationUser(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'customer/registration.html', {'form': form})
    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('auth')
        messages.error(request, 'Ошибка регистрации!')
        return render(request, 'customer/registration.html', {'form': form})

class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'customer/auth.html', {'form':form})

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, f'Добро пожаловать {form.get_user()}!')
            return redirect('customer-list')
        messages.error(request, 'Ошибка входа!')
        return render(request, 'customer/auth.html', {'form':form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('auth')





class CustomerList(ListView):
    model = Customer
    template_name = 'customer/customer.html'
    extra_context = {
        'title': model._meta.verbose_name_plural,
        'fields': model._meta.fields
    }
    paginate_by = 5

    def get_queryset(self):
        second_name =self.request.GET.get('search', '')

        if second_name:
            object_list = self.model.objects.filter(
                second_name=second_name).select_related()
            return object_list
        else:
            object_list = self.model.objects.all().select_related()
            return object_list


class ProfessionsList(ListView):
    model = Professions
    template_name = 'customer/professions.html'
    extra_context = {
        'title': model._meta.verbose_name_plural,
        'fields': model._meta.fields
    }
    paginate_by = 2

    def get_queryset(self):
        profession_name =self.request.GET.get('search', '')

        if profession_name:
            object_list = self.model.objects.filter(profession_name=profession_name)
            return object_list
        else:
            object_list = self.model.objects.all()
            return object_list



class CreateCustomer(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = CustomerForm
    template_name = 'customer/create_customer.html'
    success_url = reverse_lazy('customer-list')


class CreateProfession(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ProfessionForm
    template_name = 'customer/create_professions.html'
    success_url = reverse_lazy('professions-list')


class UpdateCustomer(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/update_customer.html'
    success_url = reverse_lazy('customer-list')

class UpdateProfession(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = Professions
    form_class = ProfessionForm
    template_name = 'customer/update_profession.html'
    success_url = reverse_lazy('professions-list')


class DeleteCustomer(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Customer
    template_name = 'customer/delete_customer.html'
    success_url = reverse_lazy('customer-list')

class DeleteProfession(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Professions
    template_name = 'customer/delete_profession.html'
    success_url = reverse_lazy('professions-list')



