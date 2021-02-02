"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', RegistrationUser.as_view(), name='registration'),
    path('auth/', Login.as_view(), name='auth'),
    path('', CustomerList.as_view(), name='customer-list'),
    path('professions/', ProfessionsList.as_view(), name='professions-list'),
    path('create_customer/', CreateCustomer.as_view(), name='create-customer'),
    path('create_profession/', CreateProfession.as_view(), name='create-profession'),
    path('update_customer/<int:pk>/', UpdateCustomer.as_view(), name='update-customer'),
    path('update_profession/<int:pk>/', UpdateProfession.as_view(), name='update-profession'),
    path('delete_customer/<int:pk>/', DeleteCustomer.as_view(),
         name='delete-customer'),
    path('delete_profession/<int:pk>/', DeleteProfession.as_view(),
         name='delete-profession'),
    path('reset_password/', ResetPassword.as_view(), name='reset-password'),
    path('change_password/', ChangePassword.as_view(), name='change-password')
]
# http://127.0.0.1:8000/update_customer/2