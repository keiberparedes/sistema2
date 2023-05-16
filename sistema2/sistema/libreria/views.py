from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio (request):
    return render(request, 'paginas/index.html')

def acerca (request):
    return render (request, 'paginas/acerca.html')

def taxis (request):
    return render (request, 'paginas/taxis.html')

def indexTaxis (request):
    return render (request, 'taxis/index.html')


