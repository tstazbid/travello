from django.shortcuts import render
from . models import Destination

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = "Dhaka"
    dest1.desc = "Popular city"
    dest1.img = "destination_1.jpg"
    dest1.price = 550

    dest2 = Destination()
    dest2.name = "Indonesia"
    dest2.desc = "Chilling area everywhere"
    dest2.img = "destination_2.jpg"
    dest2.price = 650

    dest3 = Destination()
    dest3.name = "San Francisco"
    dest3.desc = "Explore American culture"
    dest3.img = "destination_3.jpg"
    dest3.price = 700

    dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests' : dests})