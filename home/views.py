from django.shortcuts import render

# Create your views here.


def index(request):
    """Display the index page"""
    return render(request, "index.html")
