from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.forms import ModelForm
from django.db import models



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    return render(request, '../templates/login.html')


def register(request):
    if request.method == 'POST':  # If the form has been submitted...
        user = 'User: ' + request.POST.get('user_id')
        # return HttpResponse(user)
        return render(request, '../templates/home.html', {'user':user})
    else:
        return HttpResponse("not registered")
