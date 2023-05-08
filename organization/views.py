from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from organization.models import Organization
from organization.serializers import OrganizationSerializer
# Create your views here.


class OrganizationViewset(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
