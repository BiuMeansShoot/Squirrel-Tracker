from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from .models import Sighting
from .forms import SightingForm

def squirrels_map(request):
    sightings = Sighting.objects.all()[:100]
    context = {'sightings': sightings,}
    return render(request, 'sightings/map.html',context)

def all_sightings(request):
    if request.method == "GET":

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
            return redirect(f'/sightings')
    else:
        form = SightingForm()

    context = {
            'form': form,
    }

    return render(request, 'sightings/add.html', context)

def edit_sighting(request, unique_id):
    sighting = Sighting.objects.get(id=unique_id)
    if request.method == 'POST':
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

    #sighting = get_object_or_404(Sighting, pk.unique_id)
    #form = SightingForm(request,POST or None, instance=sighting)
    # if 'Update' in repost.POST:
    #    if form.is_valid():
    #        form.save()
    #        return redirect('all_sightings')
    #elif 'Delete' in request.POST:
    #    sighting.delete()
    #    return redirect('all_sightings')
    #elif 'Cancel' in request.POST:
    #    return redirect('all_sightings')
    #return render(request, 'squirreltracker/edit.html', {'form':form,})

def sightingsStats(request):
    agelist = Sighting.objects.values('age').annotate(count=Count('age'))
    colorlist = Sighting.objects.values('color').annotate(count=Count('color'))
    shiftlist = Sighting.objects.values('shift').annotate(count=Count('shift'))
    runninglist = Sighting.objects.values('running').annotate(count=Count('running'))
    chasinglist = Sighting.objects.values('chasing').annotate(count=Count('chasing'))
    context={
            'agelist':agelist,
            'colorlist':colorlist,
            'shiftlist':shiftlist,
            'runninglist':runninglist,
            'chasinglist':chasinglist,
            }
    return render(request, 'sightings/stats.html',context)


