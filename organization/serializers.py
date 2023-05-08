from rest_framework import serializers
from organization.models import Cohort, Organization, Stack


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
            "id"
            "cohort_name",
            "cohort_counter",
            "starting_date",
            "ending_date",
        ]


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = [
            "id"
            "name",
            "description",
            "starting_date",
        ]
