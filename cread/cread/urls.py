from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'regist.views.Register', name="register"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg$', 'regist.views.reg_student', name="reg_student"),

)
