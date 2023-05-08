from django.urls import include, path
from rest_framework_nested import routers
from recruitment import views
router = routers.DefaultRouter()
router.register('applications', views.ApplicationViewset,
                basename='applications')
#
urlpatterns = [
    path('', include(router.urls)),
    path('apply/', views.ApplyAPIView.as_view(), name="apply")


]
