from django.forms import ModelForm
from .models import ClientExercise

class ClientExerciseForm(ModelForm):
  class Meta:
    model = ClientExercise
    fields = ['date', 'reps', 'sets', 'time', 'note']