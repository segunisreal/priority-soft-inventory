from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView
from django.conf import settings
from django.conf.urls.static import static


def index_view(request, **kwargs):
    return JsonResponse({'detail': 'Welcome to Priority Soft!'})


urlpatterns = [
    path('', index_view),
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),

    path('doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('doc/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('doc/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
