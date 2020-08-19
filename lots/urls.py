from django.conf.urls import url
from .views import all_current_lots, all_past_lots, lot_detail, auction, bid

urlpatterns = [
    url(r'^$', all_current_lots, name='lots'),
    url(r'^pastauctions/$', all_past_lots, name='past_lots'),
    url(r'^(?P<pk>\d+)/$', lot_detail, name='lot_detail'),
    url(r'^(?P<auction_id>\d+)/edit/$', auction, name='auction'),
]
