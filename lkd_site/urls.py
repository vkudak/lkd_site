from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from jurnal.views import *
from lkd_site.settings import MEDIA_ROOT

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'lkd_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^index.html$', index),
    url(r'^journal.html$', journal),
    url(r'^contact.html$', contact),
    url(r'^about.html$', about),

    url(r'^journal/(?P<year>\d{4})/$', journal, name='journal'),
    url(r'^journal/(?P<year>\d{4})/(?P<month>\d{2})/$', journal, name='journal'),

    url(r'^auth.html$', auth),
    url(r'^logout.html$', logx),
    url(r'^admin/', include(admin.site.urls)),

    # develop
    url(r'^Observations/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
)