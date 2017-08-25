from django.conf.urls import url, include
from . import views

# app_name=main w url app_name:name

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^cv/$', views.cv, name='cv'),
    url(r'^cvdisp/$', views.CvDisp.as_view(), name='cvdisp'),
    url(r'^cvadd/$', views.cvadd, name='cvadd'),
    url(r'^(?P<numerid>[0-9]+)$', views.danedisp, name='cvpers'),

]