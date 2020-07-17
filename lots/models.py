from django.db import models
from django.utils import timezone


class Lot(models.Model):
    """Auction lot"""
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    auction_done = models.BooleanField(default=False)
    auction_end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
