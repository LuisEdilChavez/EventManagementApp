from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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