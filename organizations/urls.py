from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('organizations.views',
    (r'^$', 'index'),
    (r'^(?P<organization_id>\d+)/$', 'detail'),
)