from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', 'django_cas.views.login'),
	(r'^logout/$', 'django_cas.views.logout'),
)
