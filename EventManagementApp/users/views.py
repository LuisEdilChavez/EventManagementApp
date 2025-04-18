from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from events.models import Event
from .forms import ProfileForm

# Create views here.
def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def home_view(request):
    return render(request, 'home_page.html')



# This view displays the users dashboard, which depends on the users role (Admin or regular user) based on their credentials
def dashboard_view(request):
    user = request.user

    if user.is_superuser:
        role = "Admin"
        return render(request, 'admin_dashboard.html', {'role': role})
    else:
        role = "User"
        return render(request, 'user_dashboard.html', {'role': role})

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