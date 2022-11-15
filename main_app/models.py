from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Exercise (models.Model):
    name = models.CharField(max_length=50)
    picture = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class ClientExercise(models.Model):
    date = models.DateField()
    reps = models.IntegerField()
    sets = models.IntegerField()
    time = models.IntegerField()
    note = models.CharField(max_length=100)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"




























