from django.shortcuts import render
from products.models import Product
from lots.models import Lot


def lot_search(request):
    """Search for products by product name"""
    lots = Lot.objects.filter(name__icontains=request.GET['q'])
    return render(request, "lots.html", {"lots": lots})


def product_search(request):
    """Search for products by product name"""
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
