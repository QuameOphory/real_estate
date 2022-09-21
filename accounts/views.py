from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def register(request):
    if request.method == 'POST':
        return
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        return
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect(reverse('index'))


def dashboard(request):
    return render(request, 'accounts/dashboard.html')