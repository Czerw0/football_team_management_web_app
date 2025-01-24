from django.contrib import admin
from .models import Team, Player, Assistant, Game, Coach
# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Assistant)
admin.site.register(Game)
admin.site.register(Coach)