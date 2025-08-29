from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    #user itself. im tired
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    receive_sms = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
