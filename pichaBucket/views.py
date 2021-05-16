from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.

def landing (request):
  return render (request,'index.html')



def search_results(request):
  if 'category' in request.GET and  request.GET["category"]:
    search_term = request.GET.get("category")
    searched_images = Image.search_by_category(search_term)
    message =f"{search_term}"

    return render(request, 'search.html', {"message":message, "images":searched_images})

  else:
    message = "You havent searched for any category"

    return render(request, 'search.html', {"message":message})