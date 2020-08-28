from django.conf.urls import url
from .views import checkout_cart, checkout_auction


urlpatterns = [
    url(r'^$', checkout_cart, name='checkout_cart'),
    url(r'^(?P<auction_id>\d+)/$', checkout_auction, name='checkout_auction')
]
