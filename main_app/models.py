from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

   
class Exercise (models.Model):
    name = models.CharField(max_length=50)
    picture = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class ClientExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('2022-22-01')

    def __str__(self):
        return f"{self.user.username} - {self.date}"


class ClientExerciseLog (models.Model):
    name = models.CharField(max_length=50)
    reps = models.IntegerField()
    sets = models.IntegerField()
    time = models.IntegerField()
    note = models.CharField(max_length=100)
    client_exercise = models.ForeignKey(ClientExercise, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
