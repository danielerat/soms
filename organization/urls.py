from django.urls import include, path
from rest_framework_nested import routers
from organization import views
router = routers.DefaultRouter()
router.register('organization', views.OrganizationViewset,
                basename='organizations')
router.register('application', views.ApplicationViewset,
                basename='applications')
organization_router = routers.NestedSimpleRouter(
    router, 'organization', lookup='organization')

organization_router.register(
    'cohort', views.CohortViewset, basename='cohorts')
organization_router.register(
    'stack', views.StackViewset, basename='stacks')
organization_router.register(
    'trainer', views.TrainerViewset, basename='trainers')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(organization_router.urls)),

]
