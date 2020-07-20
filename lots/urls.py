from django.conf.urls import url
from .views import all_lots, lot_detail

urlpatterns = [
    url(r'^$', all_lots, name='lots'),
    url(r'^(?P<pk>\d+)/$', lot_detail, name='lot_detail'),
]
