from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import Context, loader

from .models import Georeference, EconomicMain, EconomicSub

# Create your views here.

# Main Page - /main/
def index(request):
    return render(request, 'index.html')

# About Us Page - /main/about_us/
def aboutus(request):
    return render(request, 'aboutus.html')

# Data and Visualize Page - /main/data&visualize/
def dataandvisualize(request):
    return render(request, "dataandvisualize.html")

# Resources Page - /main/resources/
def resources(request):
    return render(request, "resources.html")