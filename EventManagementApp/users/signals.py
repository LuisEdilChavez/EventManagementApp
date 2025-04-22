from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from twilio.rest import Client
import os

@receiver(post_save, sender=User)
def handle_user_created(sender, instance, created, **kwargs):
  if created:
    #Creates profile hopefully....
    profile = Profile.objects.create(user=instance)

    # Account registration confirmation email for the user. Gets sent to email entered.
    subject = 'Welcome the Montclair Connect!'
    message = f'Hello {instance.username},\n\nThank you for signing up to Montclair Connect!'
    from_email = 'your_email@gmail.com'
    recipient_list = [instance.email]

    # Sends SMS message
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

    send_mail(subject, message, from_email, recipient_list)
    if profile.recieve_sms and profile.phone_number:
        sms_message = f"Hello {instance.username}, Welcome to Montclair Connect, Thank You for signing up for SMS messaging. You will be notified of ongoings pertaining to Events."
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')  # or use plain strings
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

  #previous send_sms function doesnt actually work so I swapped for Twilio rest to send SMS messages to phones.
    client = Client(account_sid, auth_token)
    client.messages.create(
    body=sms_message,
    from_=twilio_number,
    to=profile.phone_number
    )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()

#combined all logic for a user creation into 1 handler, should work....