from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image, Location

# Create your views here.

def landing (request):
  images= Image.objects.all()
  location = Location.objects.all()
  title = 'Picha-Bucket'


  return render (request,'index.html',  {'title':title, 'images':images, 'location':location})



def search_results(request):
  location = Location.objects.all()
  if 'category' in request.GET and  request.GET["category"]:
    search_term = request.GET.get("category")
    searched_images = Image.search_by_category(search_term)
    message =f"{search_term}"

    return render(request, 'search.html', {"message":message, "images":searched_images,'location':location})

  else:
    message = "You havent searched for any category"

    return render(request, 'search.html', {"message":message})


def location_image(request,location_id):
  all_locations = Location.objects.all()
  location = Location.get_location_id(location_id)
  images = Image.get_image_by_location(location_id)
  places = Location.objects.all()
  place = {location} 
  message =f"{location}"
  return render(request, 'location.html', { 'location':places,'images':images,"message":message,})
  




