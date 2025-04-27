from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from .models import Event

# Create your views here.
def create_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.created_by = request.user  # Associate the event with the logged-in user
        event.save()
        return redirect('user_dashboard')  # After creating, redirect to user dashboard (or any other page)
    
    return render(request, 'events/create_event.html', {'form': form})
# home page view
def home_view(request):
    events = Event.objects.all()
    return render(request, 'home_page.html')