from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from twilio import send_sms

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
    send_mail(subject, message, from_email, recipient_list)
    if profile.recieve_sms and profile.phone_number:
        sms_message = f"Hello {instance.username}, Welcome to Montclair Connect, Thank You for signing up for SMS messaging."
        send_sms(to=profile.phone_number, message=sms_message)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()

#combined all logic for a user creation into 1 handler, should work....