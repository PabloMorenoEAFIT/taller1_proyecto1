from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
# Create your views here.

def home(request):
    # return HttpResponse('<h1>Bienvenido a la página</h1>')
    #return render(request, 'home.html', {'name': 'Pablo Moreno'})
    SearchTerm = request.GET.get('SearchMovie')
    if SearchTerm:
        movies = Movie.objects.filter(title = SearchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'SearchTerm':SearchTerm, 'movies': movies})

def about(request):
    return render(request, 'home_about.html')