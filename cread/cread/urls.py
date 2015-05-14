from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'regist.views.Register', name="register"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg$', 'regist.views.reg_student', name="reg_student"),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),


)
