from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url('^$', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]
