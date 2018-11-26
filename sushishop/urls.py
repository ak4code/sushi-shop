from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from administrator.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('menu/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('', HomeView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
