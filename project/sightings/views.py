from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count

from .models import Sighting
from .forms import SightingForm


def squirrels_map(request):
    """It is to show the map and sightings on page"""
    if request.method == "GET":
        sightings = Sighting.objects.all()[:100]
        context = {'sightings': sightings}
    return render(request, 'sightings/map.html', context)


def all_sightings(request):
    """
    This is to show the add, map, and status button on page
    and a list of unique ID
    """
    if request.method == "GET":

        sightings = Sighting.objects.all()
        context = {
            'sightings': sightings,
        }
        return render(request, 'sightings/all.html', context)


def add_sighting(request):
    """This func is to link the page to add a new sighting"""
    if request.method == 'POST' or request.method == 'GET':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightingForm()

    context = {
        'form': form,
    }

    return render(request, 'sightings/add.html', context)


def edit_sighting(request, unique_id):
    """
    The sightings/edit.html page allows user to update the info,
    and this function will redirect the page to list if the info is valid
    :param request: request from page
    :param unique_id: The unique ID of squirrel
    :return:
    """
    sighting = Sighting.objects.get(id=unique_id)
    if request.method == 'POST' or request.method == 'GET':
        form = SightingForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightingForm(instance=sighting)

    context = {
            'form': form,
    }

    return render(request, 'sightings/edit.html', context)


def sightingsStats(request):
    """It will allow the status page to show five information about squirrels"""
    agelist = Sighting.objects.values('age').annotate(count=Count('age'))
    colorlist = Sighting.objects.values('color').annotate(count=Count('color'))
    eatinglist = Sighting.objects.values('eating').annotate(count=Count('eating'))
    runninglist = Sighting.objects.values('running').annotate(count=Count('running'))
    chasinglist = Sighting.objects.values('chasing').annotate(count=Count('chasing'))
    context = {
        'agelist': agelist,
        'colorlist': colorlist,
        'eatinglist': eatinglist,
        'runninglist': runninglist,
        'chasinglist': chasinglist,
    }
    return render(request, 'sightings/stats.html', context)



