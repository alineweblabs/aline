from django.conf.urls import patterns, include, url
from django.contrib import admin 
from django.conf import settings 

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', '', name='home'),
    # url(r'^aline/', include('aline.foo.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
