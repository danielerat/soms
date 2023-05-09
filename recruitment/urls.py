from django.urls import include, path
from rest_framework_nested import routers
from recruitment import views

urlpatterns = [
    path('apply/', views.ApplyAPIView.as_view(), name="apply")
]
