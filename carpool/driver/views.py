from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import DriverForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = DriverForm()
    return render(request, 'main/profile.html', {"form":form})

