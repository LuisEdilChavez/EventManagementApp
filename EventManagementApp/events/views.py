from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from .models import Event

@login_required
def create_event(request):
    # Check if user is either admin or regular user (any authenticated user)
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated

    form = EventForm(request.POST or None)
    
    if form.is_valid():
        event = form.save(commit=False)
        event.created_by = request.user  # Associate the event with the logged-in user
        event.save()
        
        # Redirect based on role
        if request.user.is_superuser:
            return redirect('admin_dashboard')  # Admin dashboard
        else:
            return redirect('user_dashboard')  # Regular user dashboard

    return render(request, 'events/create_event.html', {'form': form})
