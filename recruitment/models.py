# Create your models here.
from django.conf import Settings
from django.db import models
from organization.models import Cohort, Stack
TRAINEE_GENDER = (
    ("M", "Male"),
    ("F", "Female"),
)


class Application(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    gender = models.CharField(
        max_length=2, choices=TRAINEE_GENDER, blank=False, null=False)
    phone_number = models.CharField(max_length=10, blank=False, null=False)
    cohort = models.ForeignKey(
        Cohort, on_delete=models.CASCADE, blank=True, null=True)
    stack = models.ForeignKey(
        Stack, on_delete=models.CASCADE, blank=True, null=True)
    resume = models.FileField(upload_to="media/applications/resume")
    province = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    dob = models.DateField()
    interviewed = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
