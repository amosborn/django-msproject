from django.conf.urls import url
from .views import all_lots

urlpatterns = [
    url(r'^$', all_lots, name='lots'),
]
