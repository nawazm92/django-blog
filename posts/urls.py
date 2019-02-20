from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.details, name='details'),
    url(r'create', views.create, name='create'),
]