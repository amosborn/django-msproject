from django.shortcuts import render
from products.models import Product
from lots.models import Lot
from django.utils import timezone


def lot_search(request):
    """Search for products by product name"""
    now = timezone.now()
    lots = Lot.objects.filter(auction_end_time__gte=now,
                              name__icontains=request.GET['q'])
    return render(request, "lots.html", {"lots": lots})


def product_search(request):
    """Search for products by product name"""
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
