from django.shortcuts import render, redirect
from .forms import UserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from events.forms import EventForm
from django.contrib.auth import authenticate, login
from django.utils import timezone  
from events.models import Event
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from twilio.rest import Client
def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user and get the user object
            user = form.save()

            # Send a welcome email to the user's email address
            send_mail(
                'Welcome to Montclair Connect! Here is a Confirmation email',
                
                settings.DEFAULT_FROM_EMAIL,  # This is your email address set in settings.py
                [user.email],  # This will be the email entered by the user
                fail_silently=False,
            )

            # Send an SMS notification to the user's phone number (if entered)
            if user.phone_number:
                sms_message = "Welcome to Montclair Connect! You've successfully registered."
                send_sms(user.phone_number, sms_message)

            messages.success(request, "Registration successful! Please check your email for confirmation.")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accountcreation/registration_page.html', {'form': form})


def home_view(request):
    return render(request, 'home_page.html')

def dashboard_view(request):
    # Show all events if admin; otherwise only user's own upcoming events
    if request.user.is_superuser:
        upcoming_events = Event.objects.filter(event_date__gte=timezone.now()).order_by('event_date')
        role = "Admin"
    else:
        upcoming_events = Event.objects.filter(
            event_date__gte=timezone.now(), created_by=request.user
        ).order_by('event_date')
        role = "User"

    # Handle event creation
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('dashboard')
    else:
        form = EventForm()

    return render(request, 'users/dashboard.html', {
        'events': upcoming_events,
        'form': form,
        'role': role
    })
@login_required
def view_profile(request):
    profile = request.user.profile
    events = Event.objects.filter(created_by=request.user)
    return render(request, 'users/profile.html', {'profile': profile, 'events': events})

@login_required
def edit_profile(request):
    profile = request.user.profile
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('view_profile')
    return render(request, 'users/edit_profile.html', {'form': form})

def login_view(request):
 if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            return render(request, 'users/login_page.html', {'error': 'Invalid credentials'})
        return render(request, 'users/login_page.html')  