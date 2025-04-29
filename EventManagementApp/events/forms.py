from django import forms
from .models import Event  # Assuming you have an Event model

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'location']  # Add fields as per your Event model

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Event Name'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Event Description'})
        self.fields['date'].widget.attrs.update({'placeholder': 'Event Date'})
        self.fields['location'].widget.attrs.update({'placeholder': 'Event Location'})
