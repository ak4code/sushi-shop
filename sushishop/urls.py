from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from administrator.views import HomeView, PageView
from .endpoints import router

admin.autodiscover()
admin.site.site_title = 'Sushi Shop'
admin.site.site_header = 'Sushi Shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('menu/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('', HomeView.as_view(), name='home'),
    path('<slug:url>/', PageView.as_view(), name='page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
