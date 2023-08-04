from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse('<h1>Bienvenido a la página</h1>')
    return render(request, 'home.html', {'name': 'Pablo Moreno'})