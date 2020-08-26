from django.conf.urls import url
from .views import about, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
]
