from django.http import Http404
from django.shortcuts import redirect, render
from .forms import PlayerForm, CoachForm
from .models import Player, Coach


def welcome_view(request):
    return render(request, "Legia/base.html")


# PLAYER VIEWS
def player_list(request):
    players = Player.objects.filter(lastname__icontains=request.POST['phrase']) if request.method == 'POST' else Player.objects.all()
    return render(request, "Legia/player/list.html", {'players': players})


def player_detail(request, id):
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        raise Http404("Player not found")
    return render(request, "Legia/player/detail.html", {'player': player})


def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save()
            return redirect('player-detail', player.id)
    else:
        form = PlayerForm()
    return render(request, "Legia/player/create.html", {'form': form})


def player_update(request, id):
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        raise Http404("Player not found")
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save()
            return redirect('player-detail', player.id)
    else:
        form = PlayerForm(instance=player)
    return render(request, "Legia/player/update.html", {'form': form})


def player_delete(request, id):
    try:
        player = Player.objects.get(id=id)
        player.delete()
    except Player.DoesNotExist:
        raise Http404("Player not found")
    return redirect('player-list')


# COACH VIEWS
def coach_list(request):
    coachs = Coach.objects.filter(lastname__icontains=request.POST['phrase']) if request.method == 'POST' else Coach.objects.all()
    return render(request, "Legia/coach/list.html", {'coachs': coachs})


def coach_detail(request, id):
    try:
        coach = Coach.objects.get(id=id)
    except Coach.DoesNotExist:
        raise Http404("Coach not found")
    return render(request, "Legia/coach/detail.html", {'coach': coach})


def coach_create(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            coach = form.save()
            return redirect('coach-detail', coach.id)
    else:
        form = CoachForm()
    return render(request, "Legia/coach/create.html", {'form': form})


def coach_update(request, id):
    try:
        coach = Coach.objects.get(id=id)
    except Coach.DoesNotExist:
        raise Http404("Coach not found")
    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coach)
        if form.is_valid():
            coach = form.save()
            return redirect('coach-detail', coach.id)
    else:
        form = CoachForm(instance=coach)
    return render(request, "Legia/coach/update.html", {'form': form})


def coach_delete(request, id):
    try:
        coach = Coach.objects.get(id=id)
        coach.delete()
    except Coach.DoesNotExist:
        raise Http404("Coach not found")
    return redirect('coach-list')
