from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


def send_application_status_email(to, names, status):
    # Render the email template
    if status:
        email_template = render_to_string(
            'emails/successful_application.html', {'names': names})
    else:
        email_template = render_to_string(
            'emails/declined_application.html', {'names': names})
    # Create an EmailMessage object
    email = EmailMessage(
        'Welcome At Streamlining Device Tracking',  # Subject of the email
        email_template,  # Content of the email (the rendered template)
        settings.DEFAULT_FROM_EMAIL,  # From email address
        [to],  # List of recipient email addresses
    )
    email.content_subtype = 'html'

    # Send the email
    email.send()
