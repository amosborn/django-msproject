from django.shortcuts import render

# Create your views here.


def index(request):
    """Display home page"""
    return render(request, 'index.html')


def about(request):
    """Display the about.html page"""
    return render(request, 'about.html')
