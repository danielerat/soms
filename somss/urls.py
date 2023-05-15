from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("recruitment/", include("recruitment.urls")),
    path("", include("organization.urls")),
    # Api Documentation Schema
    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name="schema"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
