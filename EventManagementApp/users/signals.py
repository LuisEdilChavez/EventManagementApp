from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from Twilio import send_sms

@receiver(post_save, sender=User)
def handle_user_created(sender, instance, created, **kwargs):
  if created:
    #Create profile
    Profile.objects.create(user=instance)
    
    subject = 'Welcome the Montclair Connect!'
    message = f'Hello {instance.username},\n\nThank you for signing up to Montclair Connect!'
    from_email = 'your_email@gmail.com'
    recipient_list = [instance.email]

    send_mail(subject, message, from_email, recipient_list)
    if profile.recieve.sms and profile.phone_number:
        sms_message = f"Hello {instance.username}, Welcome to Montclair Connect, Thank You for signing up for SMS messaging."
        send_sms(to=profile.phone_number, message=sms_message)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()

#combined all logic for a user creation into 1 handler, should work