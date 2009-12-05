from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('tutoring.views',
        url(r'^scrape/', 'scrape', name='tutoring-scrape'),
)
