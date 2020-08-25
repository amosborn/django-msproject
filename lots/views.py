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
    sold_auctions = Auction.objects.filter(auction_end_time__lt=now).exclude(
                                           winning_bidder=7)
    unsold_auctions = Auction.objects.filter(auction_end_time__lt=now,
                                             winning_bidder=7)
    return render(request, 'pastlots.html', {'sold_auctions': sold_auctions,
                  'unsold_auctions': unsold_auctions})


def past_lot_detail(request, pk):
    """Return individual expired lot with auction results"""


def lot_detail(request, lot_id):
    """Render lot detail page and create auction with default values"""

    lot = get_object_or_404(Lot, id=lot_id)
    auction = Auction.objects.filter(lot=lot_id)

    if lot:
        if auction:
            auction = auction
        else:
            auction_default = Auction()
            auction_default.lot = lot
            auction_default.number_of_bids = 0
            auction_default.winning_bidder = get_object_or_404(
                                             User, username='Admin')
            auction_default.winning_bid = 0.00
            auction_default.auction_end_time = lot.auction_end_time
            auction_default.save()

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
            bid_default.user = get_object_or_404(User, username='Admin')
            bid_default.auction = auction
            bid_default.bid_amount = 0.00
            bid_default.save()
            latest_bid = bid_default

    return render(request, 'bidform.html', {'auction': auction,
                  'latest_bid': latest_bid, 'bid_form': bid_form})


@login_required
def bid(request, auction_id):
    """Place a bid"""

    auction = get_object_or_404(auction_id)
    bid = Bid.objects.filter(auction=auction_id).order_by('-bid_time')
    current_bid = bid[0].bid_amount
    bidder = auth.get_user(request)
    bid_form = BidForm(request.POST, request.FILES, instance=bid)

    if request.method == 'POST':

        if bid_form.is_valid():
            new_bid = bid_form.save()
            if current_bid < bid_form.cleaned_data['bid_amount']:
                new_bid.user = bidder
                new_bid.auction = auction
                new_bid.bid_amount = bid_form.cleaned_data['bid_amount']
                new_bid.bid_time = datetime.now()
                auction.number_of_bids += 1
                auction.winning_bid = bid_form.cleaned_data['bid_amount']
                auction.winning_bidder = bidder
                new_bid.save()
                auction.save()
                return redirect(auction, auction_id=auction_id)
            else:
                return redirect(auction, auction_id=auction_id)

    else:
        bid_form = BidForm(instance=bid)

    return render(request, 'bidform.html', {'bid_form': bid_form})
