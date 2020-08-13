from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Lot(models.Model):
    """Auction lot"""
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    auction_done = models.BooleanField(default=False)
    auction_end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Auction(models.Model):
    """Auction model"""
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField(default=0)
    winning_bidder = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    winning_bid = models.IntegerField(default=0)
    auction_end_time = models.DateTimeField(blank=True, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "Auction: " + str(self.pk) + " Lot: " + str(self.lot.name)


class Bid(models.Model):
    """Auction bid model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bid_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Bid: " + str(self.pk) + " Lot: " + str(self.lot.name)
