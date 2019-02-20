from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import signup_page_view

urlpatterns = [
    url('^$', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('account/', include('django.contrib.auth.urls')),
    url(r'^signup/$', signup_page_view, name='signup'),
]
