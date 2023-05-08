from rest_framework import serializers
from organization.models import Cohort, Organization, Stack, Trainee, Trainer


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "id",
            "name",
            "description",
            "website",
            "country",
            "province",
            "district",
            "sector",
            "address",
            "logo",
            "phone_number"
        ]


class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = [
            "id",
            "cohort_name",
            "cohort_counter",
            "starting_date",
            "ending_date",
        ]

    def create(self, validated_data):
        organization_id = self.context['organization_pk']
        return Cohort.objects.create(organization_id=organization_id, **validated_data)


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = [
            "id",
            "name",
            "description",
            "starting_date",
        ]

    def create(self, validated_data):
        organization_id = self.context['organization_pk']
        return Stack.objects.create(organization_id=organization_id, **validated_data)

# Trainer serialzier


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = [
            "id"
            "user",
            "first_name",
            "last_name",
            "email",
            "gender",
            "phone_number",
            "stack",
            "resume",
            "province",
            "district",
            "dob",
        ]

# Trainee serializer


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = [
            "id"
            "user",
            "first_name",
            "last_name",
            "email",
            "gender",
            "phone_number",
            "cohort",
            "stack",
            "resume",
            "province",
            "district",
            "dob",
        ]
