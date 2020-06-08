from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.


def index(request):
    """Return index.html page"""
    return render(request, 'index.html')


def logout(request):
    """Log user out"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(reverse('index'))
