from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """Renders cart contents page"""
    return render(request, 'cart.html')
