from django.forms import ModelForm
from .models import ClientExercise

class ClientExerciseForm(ModelForm):
  class Meta:
    model = ClientExercise
    fields = ['reps', 'sets', 'time', 'note']