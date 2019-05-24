from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import signup_page_view

urlpatterns = [
    url('^', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', signup_page_view, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)