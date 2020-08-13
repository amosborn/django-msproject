from django.contrib import admin
from .models import Lot, Bid, Auction


admin.site.register(Lot)
admin.site.register(Bid)
admin.site.register(Auction)
