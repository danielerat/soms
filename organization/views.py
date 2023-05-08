from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from organization.models import Cohort, Organization, Stack
from organization.serializers import CohortSerializer, OrganizationSerializer, StackSerializer
# Create your views here.


class OrganizationViewset(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()


class CohortViewset(ModelViewSet):
    serializer_class = CohortSerializer

    def get_queryset(self):
        return Cohort.objects.filter(organization_id=self.kwargs['organization_pk'])

    def get_serializer_context(self):
        # Get the image id and send it in the backend
        return {"organization_pk": self.kwargs["organization_pk"]}


class StackViewset(ModelViewSet):
    serializer_class = StackSerializer

    def get_queryset(self):
        return Stack.objects.filter(organization_id=self.kwargs['organization_pk'])

    def get_serializer_context(self):
        return {"organization_pk": self.kwargs["organization_pk"]}
