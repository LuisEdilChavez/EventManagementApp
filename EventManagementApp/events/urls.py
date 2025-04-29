# events/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('list/', views.event_list, name='event_list'),
    path('users/', include('users.urls')),

]
