from django.shortcuts import render
from grallery.models import Grallery

def home(request):
    grallerys = Grallery.objects
    return render(request, 'home.html',{'grallerys':grallerys})