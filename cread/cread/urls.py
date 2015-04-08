from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'reg/$', 'regist.views.Register', name="register"),
    url(r'^admin/', include(admin.site.urls)),
)
