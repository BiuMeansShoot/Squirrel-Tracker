from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Sighting
from .forms import SightingForm

def index(request):
    return HttpResponse('Hi')
# Create your views here.
