from django.urls import path
from users.views import registration_view, home_view, dashboard_view, login_view
from django.contrib.auth import views as auth_views
from .import views
# took a while for me to realize I mispelled register, 
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.registration_view, name='register'),
]
