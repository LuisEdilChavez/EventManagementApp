"""
URL configuration for EventManagementApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import home_view, dashboard_view
from django.conf import settings
from django.conf.urls.static import static
# Make sure to import the view names from views.py, Add a comma and the views name to the import.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),  # connects /accounts/ to your registration/login views
    path('', home_view, name='home'), # makes the / show the homepage.
    path('dashboard/', dashboard_view, name='dashboard'), # dashboard view
    path('events/', include('events.url')), #Include events 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
