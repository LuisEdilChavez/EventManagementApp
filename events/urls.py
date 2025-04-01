from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Calls the 'home' view when visiting the main page
]
