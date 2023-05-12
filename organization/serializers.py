from rest_framework import serializers

from authentication.models import User

from django.db import transaction
from organization.models import Cohort, Organization, Stack, Trainee, Trainer, Outsource

from recruitment.models import Application


class SimpleUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['first_name', 'last_name',

                  'email', 'phone_number']


class OrganizationSerializer(serializers.ModelSerializer):

    cohorts = serializers.StringRelatedField(many=True)

    stacks = serializers.StringRelatedField(many=True)

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

            "phone_number",

            "cohorts",

            "stacks",

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

    user = SimpleUserSerializer(read_only=True)

    class Meta:

        model = Trainer

        fields = [
            "id",

            "user",

            "gender",

            "stack",

            "resume",

            "province",
            "district",

            "dob",

        ]

    def create(self, validated_data):

        organization_id = self.context['organization_pk']

        return Trainer.objects.create(organization_id=organization_id, **validated_data)


# Trainee serializer


class TraineeSerializer(serializers.ModelSerializer):

    user = SimpleUserSerializer(read_only=True)

    class Meta:

        model = Trainee

        fields = [
            "id",

            "user",

            "gender",

            "cohort",

            "stack",

            "resume",

            "province",
            "district",

            "dob",

        ]

    def create(self, validated_data):
        organization_id = self.context['organization_pk']
        return Trainee.objects.create(organization_id=organization_id, **validated_data)


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Application

        fields = [
            "id",

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

            "interviewed",

            "application_status"

        ]

        extra_kwargs = {

            'first_name': {'read_only': True},

            'last_name': {'read_only': True},

            'email': {'read_only': True},

            'gender': {'read_only': True},

            'phone_number': {'read_only': True},

            'resume': {'read_only': True},

            'province': {'read_only': True},

            'district': {'read_only': True},

            'dob': {'read_only': True},

        }


class OutsourceSerializer(serializers.ModelSerializer):
    class Meta:
        jls_extract_var = Outsource
        model = jls_extract_var


class OutsourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outsource
        fields = [
            "id",
            "organization",
            "user",
            "outsource_to",
            "date",
        ]
        extra_kwargs = {
            'organization': {'read_only': True},
            'user': {'read_only': True},
        }

    def validate(self, data):
        organization_pk = self.context.get('organization_pk')
        trainee_pk = self.context.get('trainee_pk')
        if not Organization.objects.filter(pk=organization_pk).exists():
            raise serializers.ValidationError(
                "Unknown Organization.")
        if not Trainee.objects.filter(pk=trainee_pk).exists():
            raise serializers.ValidationError(
                "Unknown Trainee.")
        return data

    def save(self, **kwargs):
        organization_pk = self.context.get('organization_pk')
        trainee_pk = self.context.get('trainee_pk')
        outsource_to = self.validated_data['outsource_to']
        # If one fails then other fails too.
        with transaction.atomic():
            # We have a cart item, Update it.
            user = Trainee.objects.get(pk=trainee_pk).user
            outsource = Outsource.objects.create(
                organization_id=organization_pk,
                user=user,
                outsource_to=outsource_to
            )
            self.instance = outsource
        return self.instance
