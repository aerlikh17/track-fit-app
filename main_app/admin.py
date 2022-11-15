from django.contrib import admin
from .models import Exercise, ClientExercise, ClientExerciseLog

# Register your models here.
admin.site.register(Exercise)
admin.site.register(ClientExercise)
admin.site.register(ClientExerciseLog)


