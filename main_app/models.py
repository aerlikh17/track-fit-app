from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Exercise (models.Model):
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

    picture = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    picture = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class ClientExercise(models.Model):
    date = models.DateField('2022-22-01')
    reps = models.IntegerField()
    sets = models.IntegerField()
    time = models.IntegerField()
    note = models.CharField(max_length=100)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"




























