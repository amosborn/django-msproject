from django.shortcuts import render

# Create your views here.


def about(request):
    """Display the about.html page"""
    return render(request, 'about.html')
