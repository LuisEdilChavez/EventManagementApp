from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    #user itself
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    
    #SMS and phonenumber thats attached to account
    receive_sms = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # User uploaded avatar and profile banner.
    avatar = models.ImageField(upload_to='avatars/', default='avatar/default.jpg', blank = True)
    banner = models.ImageField(upload_to='banners/', default='banners/default.jpg', blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
