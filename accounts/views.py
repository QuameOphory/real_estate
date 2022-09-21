from email import message
import re
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The Email is already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        first_name = first_name,
                        last_name = last_name,
                        email = email,
                        password = password
                    )
                    user.save()
                    messages.success(request, 'You account has been registered successfully')
                    return redirect('login')
        else:
            messages.error(request, 'The passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credientials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(
            request,
            'You are logged out successfully'
        )
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')