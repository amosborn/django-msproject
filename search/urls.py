from django.conf.urls import url
from .views import product_search, lot_search


urlpatterns = [
    url(r'^lotsearch/$', lot_search, name='lot_search'),
    url(r'^productsearch/$', product_search, name='product_search'),
]
