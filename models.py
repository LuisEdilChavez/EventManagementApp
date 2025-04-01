from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=150, unique = True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=128)

#Setup the login info in models for the event app.
#LUISCHAVEZ 3/30/2025 4:30 pm

