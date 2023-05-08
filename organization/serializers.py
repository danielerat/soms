from rest_framework import serializers
from organization.models import Organization


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
