from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("recruitment/", include("recruitment.urls")),
    path("", include("organization.urls")),
]
