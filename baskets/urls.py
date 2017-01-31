from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from baskets.views import BasketListView, BasketDetailView


urlpatterns = [
    url(r'^$', BasketListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', BasketDetailView.as_view(), name='detail'),
]