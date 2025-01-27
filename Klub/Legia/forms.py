from django import forms
from .models import Player, Coach, Assistant, Team, Game


class PlayerForm(forms.ModelForm):
   class Meta:
     model = Player
     fields = '__all__'

class CoachForm(forms.ModelForm):
   class Meta:
     model = Coach
     fields = '__all__'

class AssistantForm(forms.ModelForm):
   class Meta:
     model = Assistant
     fields = '__all__'

class TeamForm(forms.ModelForm):
   class Meta:
     model = Team
     fields = '__all__'

class GameForm(forms.ModelForm):

    class Meta:
      model = Game
      fields = '__all__'