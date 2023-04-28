
# Create your models here.
from django.conf import settings
from django.db import models
TRAINEE_GENDER = (
    ("M", "Male"),
    ("F", "Female"),
)

# Solvit/ Enterprise models


class Cohort(models.Model):
    cohort_name = models.CharField(max_length=255)
    cohort_counter = models.IntegerField()
    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()




# Keeps track of all stacks of a given cohorts
class Stack(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    starting_date = models.DateTimeField()

# Keeps track of a given organization


class Organization(models.Model):
    name = models.CharField(max_length=244)
    description = models.TextField()
    website = models.URLField()
    country = models.CharField(max_length=244)
    province = models.CharField(max_length=244)
    district = models.CharField(max_length=244)
    sector = models.CharField(max_length=244)
    address = models.CharField(max_length=244)
    logo = models.ImageField(default="default.jpg",
                             upload_to=f"media/organization")
    phone_number = models.CharField(max_length=244)


class OrganizationPosition(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="position", on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=244)
    since = models.DateField()
# -----------------------------------------------------
# Peopler Who are Training in the cohort


class Trainer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="trainer", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    gender = models.CharField(
        max_length=2, choices=TRAINEE_GENDER, blank=False, null=False)
    phone_number = models.CharField(max_length=10, blank=False, null=False)
    stack = models.ForeignKey(
        Stack, on_delete=models.CASCADE, blank=True, null=True)
    resume = models.FileField(upload_to="media/applications/resume")
    province = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    dob = models.DateField()

# -----------------------------------------------------
# people who are being trained by trainee


class Trainee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="trainee", on_delete=models.CASCADE)
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
