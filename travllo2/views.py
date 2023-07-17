from django.shortcuts import render
from .models import Destination

# Create your views here.

def destinations(request):
    return render(request, 'destinations.html')

def index(request):


    distinations = Destination.objects.all()

    return render(request, 'index.html', {'distinations': distinations})
