from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from organization.models import Cohort, Organization, Stack, Trainer, Trainee
from organization.serializers import ApplicationSerializer, CohortSerializer, OrganizationSerializer, StackSerializer, TrainerSerializer, TraineeSerializer, OutsourceSerializer
from recruitment.models import Application
from rest_framework.response import Response
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


class TrainerViewset(ModelViewSet):
    serializer_class = TrainerSerializer

    def get_queryset(self):
        return Trainer.objects.filter(organization_id=self.kwargs['organization_pk'])

    def get_serializer_context(self):
        return {"organization_pk": self.kwargs["organization_pk"]}


class TraineeViewset(ModelViewSet):
    serializer_class = TraineeSerializer

    def get_queryset(self):

        return Trainee.objects.filter()

    @action(detail=True, methods=['post'])
    def outsource(self, request, organization_pk=None, pk=None):
        serializer = OutsourceSerializer(
            data=request.data, context={"organization_pk": organization_pk, "trainee_pk": pk, "request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Trainee Oursourced Successfully.'})


class ApplicationViewset(ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
