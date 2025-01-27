from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PlayerForm, CoachForm, AssistantForm, TeamForm, GameForm
from .models import Player, Coach, Assistant, Team, Game


def welcome_view(request):
    return render(request, "Legia/base.html")



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

def assistant_list(request):
    assistants = Assistant.objects.filter(lastname__icontains=request.POST['phrase']) if request.method == 'POST' else Assistant.objects.all()
    return render(request, "Legia/assistant/list.html", {'assistants': assistants})


def assistant_detail(request, id):
    try:
        assistant = Assistant.objects.get(id=id)
    except Assistant.DoesNotExist:
        raise Http404("Assistant not found")
    return render(request, "Legia/assistant/detail.html", {'assistant': assistant})


def assistant_create(request):
    if request.method == 'POST':
        form = AssistantForm(request.POST)
        if form.is_valid():
            assistant = form.save()
            return redirect('assistant-detail', assistant.id)
    else:
        form = AssistantForm()
    return render(request, "Legia/assistant/create.html", {'form': form})


def assistant_update(request, id):
    try:
        assistant = Assistant.objects.get(id=id)
    except Assistant.DoesNotExist:
        raise Http404("Assistant not found")
    if request.method == 'POST':
        form = AssistantForm(request.POST, instance=assistant)
        if form.is_valid():
            assistant = form.save()
            return redirect('assistant-detail', assistant.id)
    else:
        form = AssistantForm(instance=assistant)
    return render(request, "Legia/assistant/update.html", {'form': form})


def assistant_delete(request, id):
    try:
        assistant = Assistant.objects.get(id=id)
        assistant.delete()
    except Assistant.DoesNotExist:
        raise Http404("Assistant not found")
    return redirect('assistant-list')


def team_list(request):
    teams = Team.objects.all()

    for team in teams:
        team.player_count = team.players.count()  
    return render(request, "Legia/team/list.html", {'teams': teams})


def team_detail(request, id):
    team = get_object_or_404(Team, id=id)
    players = team.players.all()  

    return render(request, "Legia/team/detail.html", {'team': team, 'players': players})



def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect('team-detail', team.id)
    else:
        form = TeamForm()
    return render(request, "Legia/team/create.html", {'form': form})


def team_update(request, id):
    try:
        team = Team.objects.get(id=id)
    except Team.DoesNotExist:
        raise Http404("Team not found")
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save()
            return redirect('team-detail', team.id)
    else:
        form = TeamForm(instance=team)
    return render(request, "Legia/team/update.html", {'form': form})


def team_delete(request, id):
    try:
        team = Team.objects.get(id=id)
        team.delete()
    except Team.DoesNotExist:
        raise Http404("Team not found")
    return redirect('team-list')

def team_player_count(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        raise Http404("Team not found")
    player_count = Player.objects.filter(team=team).count()

    return render(request, "Legia/team/detail.html", {
        'team': team,
        'player_count': player_count
    })



def game_list(request):
    game = Game.objects.filter(opponent__icontains=request.POST['phrase']) if request.method == 'POST' else Game.objects.all()
    return render(request, "Legia/game/list.html", {'games': game})


def game_detail(request, id):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404("Assistant not found")
    return render(request, "Legia/game/detail.html", {'game': game})


def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('game-detail', game.id)
    else:
        form = GameForm()
    return render(request, "Legia/game/create.html", {'form': form})



def game_update(request, id):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404("Game not found")
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save()
            return redirect('game-detail', game.id)
    else:
        form = GameForm(instance=game)
    return render(request, "Legia/game/update.html", {'form': form})


def game_delete(request, id):
    try:
        game = Game.objects.get(id=id)
        game.delete()
    except Game.DoesNotExist:
        raise Http404("Game not found")
    return redirect('game-list')
