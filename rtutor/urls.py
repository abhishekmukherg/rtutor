"""
URLs File
"""

from django.conf.urls.defaults import patterns, include
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^tutoring/', include('tutoring.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/login/$', 'django_cas.views.login'),
    (r'^accounts/logout/$', 'django_cas.views.logout'),
#    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
#    (r'^accounts/', include('userprofile.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
