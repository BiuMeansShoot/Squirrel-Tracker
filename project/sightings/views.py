from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Sighting
from .forms import SightingForm

def all_sightings(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request,'sightings/all.html', context)


def add_sighting(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/list/')
    else:
        form = SightingForm()

    context = {
            'form': form,
    }

    return render(request, 'sightings/add.html', context)
# Create your views here.
