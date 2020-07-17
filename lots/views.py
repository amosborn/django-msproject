from django.shortcuts import render
from .models import Lot

# Create your views here.


def all_lots(request):
    lots = Lot.objects.all()
    return render(request, 'lots.html', {'lots': lots})
