# events/forms.py

from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date']  # adjust fields as needed
 
# a class that renders HTML form field, validate data and save it.