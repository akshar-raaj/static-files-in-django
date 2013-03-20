from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
        url(r'^home$', direct_to_template, {"template": "other_app/home.html"})
)
