from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cshipman2.views.home', name='home'),
    url(r'^blog/', 'blog.views.home'),
    # url(r'^cshipman2/', include('cshipman2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation: ddfg
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
