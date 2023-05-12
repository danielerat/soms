from rest_framework import serializers, status
from recruitment.models import Application

import re


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

    def validate(self, data):
        if not re.match(r'^\d{10}$', data['phone_number']):
            raise serializers.ValidationError('Phone Number is Invalid')
        # Get the phone number since it's unique
        applicant = Application.objects.filter(
            phone_number=data['phone_number'])
        if applicant.exists():
            print(applicant.first())
            if applicant.first().application_status == "D":
                raise serializers.ValidationError(
                    'You were Not Selected for this Cohort.')
            raise serializers.ValidationError(
                'Your Application is being reviewed.')
        return data
