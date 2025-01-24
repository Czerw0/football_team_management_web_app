from django import forms
from .models import Player, Coach, Assistant


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