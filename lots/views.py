from django.shortcuts import render,  get_object_or_404
from .models import Lot

# Create your views here.


def all_lots(request):
    """Return all lots"""
    lots = Lot.objects.all()
    return render(request, 'lots.html', {'lots': lots})


def lot_detail(request, pk):
    """Return individual lot object and render it to lotdetail.html page"""
    lot = get_object_or_404(Lot, pk=pk)
    return render(request, "lotdetail.html", {'lot': lot})
