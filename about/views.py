from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_about(request):
    return render(request, 'home_about.html')