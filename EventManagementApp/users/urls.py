from django.urls import path
from .views import registration_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration/', registration_view, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='login_page.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #Logout URL
]
