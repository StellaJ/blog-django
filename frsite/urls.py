from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'frsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stelka/', include('stelka.urls')),
    url(r'^blog/', include('blog.urls')),

)
