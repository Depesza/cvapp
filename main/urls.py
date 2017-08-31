from django.conf.urls import url
from . import views

# app_name=main w url app_name:name


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^logout/$', views.logoutView, name='logout'),

    url(r'^cv/$', views.cv, name='cv'),
    url(r'^cvdisp/$', views.CvDisp.as_view(), name='cvdisp'),
    url(r'^cvdispdef/$', views.CvDispDef, name='cvdispdef'),
    url(r'^(?P<pk>[0-9]+)$', views.DaneDisp.as_view(), name='cvpers'),
    url(r'^add/$', views.CvCreate.as_view(), name='cvcreate'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.CvEdit.as_view(), name='cvedit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.CvDelete.as_view(), name='cvdelete'),
]