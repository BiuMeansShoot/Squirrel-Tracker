from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
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

def edit_sighting(request, unique_id):
    sighting = get_object_or_404(Sighting, pk.unique_id)
    form = SightingForm(request,POST or None, instance=sighting)
    if 'Update' in repost.POST:
        if form.is_valid():
            form.save()
            return redirect('all_sightings')
    elif 'Delete' in request.POST:
        sighting.delete()
        return redirect('all_sightings')
    elif 'Cancel' in request.POST:
        return redirect('all_sightings')
    return render(request, 'squirreltracker/edit.html', {'form':form,})

def sightingsStats(request):
    agelist = Sighting.objects.values('age').annotate(count=Count('age')).orber_by()
    colorlist = Sighting.objects.values('color').annotate(count=Count('color')).order_by()
    datelist = Sighting.objects.values('date').annotate(count=Count('date')).order_by()
    runninglist = Sighting.objects.values('running').annotate(count=Count('running')).order_by()
    chasinglist = Sighting.objects.values('chasing').annotate(count=Count('chasing')).order_by()
    context={
            'agelist':agelist,
            'shiftlist':shiftlist,
            'runninglist':runninglist,
            'chasinglist':chasinglist,
            }
    return render(request, 'stats.html',context)


