from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    unitType = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    picture = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.name

class ClientExercise(models.Model):
    Date = models.DateField('2022-22-01')
    Note = models.CharField(max_length=100)
    unitAmount1 = models.IntegerField()
    unitAmount2 = models.IntegerField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

