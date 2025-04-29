from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from twilio.rest import Client
import os
#Creates user profile and will send confirmation email
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)

        # Send welcome email
        if instance.email:
            send_mail(
                subject='Welcome to Montclair Connect!',
                message=f'Hello {instance.username},\n\nThank you for signing up for Montclair Connect!',
                from_email=os.getenv('DEFAULT_FROM_EMAIL', 'your_email@gmail.com'),  # safer fallback
                recipient_list=[instance.email],
                fail_silently=True,  # Avoid crashing if email fails
            )

        # Send SMS if opted-in (initially new users won't have opted-in yet)
        if profile.receive_sms and profile.phone_number:
            account_sid = os.getenv('TWILIO_ACCOUNT_SID')
            auth_token = os.getenv('TWILIO_AUTH_TOKEN')
            twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

            if account_sid and auth_token and twilio_number:
                try: # should work hopefully?
                    client = Client(account_sid, auth_token)
                    client.messages.create(
                        body=f"Hello {instance.username}, welcome to Montclair Connect! Thank you for signing up for SMS notifications.",
                        from_=twilio_number,
                        to=profile.phone_number
                    )
                except Exception as e:
                    print(f"SMS sending failed: {e}")
# saves user profile settings etccc
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
