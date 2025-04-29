# events/urls.py
from django.urls import path, include
from . import views
from users.views import home_view

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('', home_view, name='home')
]
