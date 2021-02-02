from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def hi(request):
    return HttpResponse('My first app')

def index(request):
    my_list = list(range(10))
    context = {
        'name': 'First app',
        'title':'My app',

    }
    return render(request, context=context)