from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Class for event 
class Event(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  event_date = models.DateTimeField()
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def _str_(self):
    return self.title 
# This is data structure for the event.
# It will have a Title, Description, Who posted/created, Time and date of event
# Straigt forward approach.
# When we do startapp we tell django that we are making a new feature on the same level/dir as manage.py