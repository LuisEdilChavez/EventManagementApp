from django.shortcuts import render

# Handles requests & returns responses (HTML, JSON, etc.)
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Event Management App!")
