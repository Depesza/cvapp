from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cv/$', views.cv),
    url(r'^cvdisp/$', views.cvdisp),
    url(r'^cvadd/$', views.cvadd),

]