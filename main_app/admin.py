from django.contrib import admin
from .models import Exercise, Client, ClientExercise

# Register your models here.
admin.site.register(Exercise)
admin.site.register(Client)
admin.site.register(ClientExercise)


