from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from commom.views import EmailAPIView, PasswordResetRequestView, PasswordResetConfirmView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/clinics/', include('clinic.urls')),
    path('api/send-email/', EmailAPIView.as_view(), name='send-email'),
    path('api/password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('api/password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/institucional/', include('institucional.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
