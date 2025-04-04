from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'password') #Display these fields in the admin list
  search_fields = ('username', 'email') # searchs for a username/email