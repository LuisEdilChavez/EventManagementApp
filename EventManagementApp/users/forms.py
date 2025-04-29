from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# Lets users set username email and password and phonenumber / recieve SMS
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    receive_sms = forms.BooleanField(required=False, label="Opt-in for SMS notifications")
    help_texts = {
            'username': '150 characters max, letters, digits.',
            'email': 'Enter a valid email address.',
            'password1': 'At least 8 characters, avoid common passwords.',
            'password2': 'Confirm your password.',
            'phone_number': 'Include country code, e.g., +1234567890.',
            'receive_sms': 'Opt-in for SMS notifications.',
        }
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            # Save Profile fields
            profile = Profile.objects.get_or_create(user=user)
            profile.phone_number = self.cleaned_data.get('phone_number')
            profile.receive_sms = self.cleaned_data.get('receive_sms')
            profile.save()

        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'receive_sms', 'avatar', 'banner']
