from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.contrib import auth
from .models import Lot, Bid, Auction
from .forms import BidForm


# Create your views here.


def all_current_lots(request):
    """Return all current auction lots"""
    now = timezone.now()
    lots = Lot.objects.filter(auction_end_time__gte=now)
    return render(request, 'lots.html', {'lots': lots})


def all_past_lots(request):
    """Return all past auction lots"""
    now = timezone.now()
    pastlots = Lot.objects.filter(auction_end_time__lt=now)
    return render(request, 'pastlots.html', {'pastlots': pastlots})


def lot_detail(request, pk):
    """Return individual lot object and render it to lotdetail.html page"""
    lot = get_object_or_404(Lot, pk=pk)
    return render(request, 'lotdetail.html', {'lot': lot})


@login_required
def auction(request, auction_id):
    """Render auction and bidding page"""

    auction = get_object_or_404(Auction, id=auction_id)
    bid = Bid.objects.filter(auction=auction_id).order_by('-bid_time')
    bid_form = BidForm
    
    if auction:
        if bid:
            latest_bid = bid[0]
        else:
            bid_default = Bid()
            bid_default.user = get_object_or_404(User, id=1)
            bid_default.auction = auction
            bid_default.bid_amount = 0.00
            bid_default.save()
            latest_bid = bid_default

    return render(request, 'bidform.html', {'auction': auction,
                  'latest_bid': latest_bid, 'bid_form': bid_form})
