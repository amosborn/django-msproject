from django.conf.urls import url
from .views import view_cart, add_product_to_cart, adjust_cart, \
    add_auction_to_cart


urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<auction_id>\d+)', add_auction_to_cart,
        name='add_auction_to_cart'),
    url(r'^add/(?P<product_id>\d+)', add_product_to_cart,
        name='add_product_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]
