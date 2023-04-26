
# Create your models here.
from django.conf import settings
from django.db import models


# Solvit/ Enterprise models

class Cohort(models.Model):
    cohort_name = models.CharField(max_length=255)
    cohort_counter = models.IntegerField()
    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()


# Keeps track of all stacks of a given cohorts
class Stacks(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    starting_date = models.DateTimeField()

# Keeps track of a given organization


class Organization(models.Model):
    name = models.CharField(max_length=244)
    description = models.TextField()
    website = models.URLField()
    country = models.CharField(100)
    province = models.CharField(100)
    district = models.CharField(100)
    sector = models.CharField(100)
    address = models.CharField(100)
    logo = models.ImageField(default="default.jpg",
                             upload_to=f"media/organization")
    phone_number = models.CharField(max_length=244)


class OrganizationPosition(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    title = models.CharField()
    since = models.DateField()

# -----------------------------------------------------
