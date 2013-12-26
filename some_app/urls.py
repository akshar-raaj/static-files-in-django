from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from .views import HomeView

urlpatterns = patterns('',
    url(r'^home$', cache_page(HomeView.as_view(), 60)),
)
