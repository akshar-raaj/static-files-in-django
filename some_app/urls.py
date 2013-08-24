from django.conf.urls import patterns, include, url

from .views import HomeView

urlpatterns = patterns('',
    url(r'^home$', HomeView.as_view()),
)
