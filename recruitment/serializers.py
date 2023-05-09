from rest_framework import serializers
from recruitment.models import Application


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
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
