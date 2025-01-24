from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
import datetime

from .forms import PlayerForm
from .models import Player


def welcome_view(request):
    return render(request,
                  "Legia/base.html")


('player-list')
def player_list(request):
    # jeżeli POST to znaczy, że wybrano opcję wyszukania obiektów
    if request.method == 'POST':
        players = Player.objects.filter(lastname__icontains=request.POST['phrase'])
    else:
        # pobieramy wszystkie obiekty Person z bazy poprzez QuerySet
        players = Player.objects.all()

    return render(request,
                  "Legia/player/list.html",
                  {'players': players})  # Zmieniono klucz na 'players'


def player_detail(request, id):
    # pobieramy konkretny obiekt Person
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        raise Http404("Obiekt Player o podanym id nie istnieje")

    return render(request,
                  "Legia/player/detail.html",
                  {'player': player})


def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            # zapisujemy obiekt do bazy
            player = form.save()
            # po dodaniu nastąpi przekierowanie do strony szczegółów tego obiektu
            return redirect('player-detail', player.id)
    else:
        form = PlayerForm()

    return render(request,
                'Legia/player/create.html',
                {'form': form})


def player_update(request, id):
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        raise Http404("Obiekt Player o podanym id nie istnieje")

    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            # zapisujemy obiekt do bazy
            player = form.save()
            # po dodaniu nastąpi przekierowanie do strony szczegółów tego obiektu
            return redirect('player-detail', player.id)
    else:
        form = PlayerForm(instance=player)
        
    form = PlayerForm(instance=player)
    return render(request,
                    'Legia/player/update.html',
                    {'form': form})


def player_delete(request, id):
    try:
        player = Player.objects.get(id=id)
        player.delete()
    except Player.DoesNotExist:
        raise Http404("Obiekt Player o podanym id nie istnieje")

    return redirect('player-list')