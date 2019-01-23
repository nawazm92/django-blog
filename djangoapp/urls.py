from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import about_page_view

urlpatterns = [
    url('^$', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    url(r'^about', about_page_view, name='about')
]
