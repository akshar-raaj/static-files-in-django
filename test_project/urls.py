from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^some_app/', include('some_app.urls')),
    url(r'^other_app/', include('other_app.urls')),
)
