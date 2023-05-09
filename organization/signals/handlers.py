from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from organization.utils.send_email_templates import send_welcome_email
from recruitment.models import Application
from authentication.models import User
from organization.models import Cohort, Organization, Trainee


@receiver(post_save, sender=Application)
def change_device_transfer_status(sender, instance, created, **kwargs):
    if not created:
        # User Accepts the device.
        if instance.application_status == "A":
            with transaction.atomic():
                # Create the new participat a user account.
                user = User.objects.create(
                    first_name=instance.first_name,
                    last_name=instance.last_name,
                    email=instance.email,
                    phone_number=instance.phone_number
                )
                # Get the first cohort
                cohort = Cohort.objects.last()

                # Get the first organizaiton
                organization = Organization.objects.first()
                Trainee.objects.create(
                    organization=organization,
                    user=user,
                    cohort=cohort,
                    gender=instance.gender,
                    stack=instance.stack,
                    resume=instance.resume,
                    province=instance.province,
                    district=instance.district,
                    dob=instance.dob
                )
                try:
                    send_welcome_email(user.email, user.get_full_name())
                except:
                    print("Email could not be sent")
                # Delete the pending device
                instance.delete()
        # if instance.transfer_status == "D":
        #     # instance.delete()
