from django.urls import include, path
from rest_framework_nested import routers
from organization import views
router = routers.DefaultRouter()
router.register('organization', views.OrganizationViewset,
                basename='organizations')
#
urlpatterns = [
    path('', include(router.urls)),
]
