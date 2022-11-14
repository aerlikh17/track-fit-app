from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# class Exercise(models.Model):
#     name = models.CharField(max_length=50)
#     unitType = models.CharField(max_length=50)
#     Description = models.CharField(max_length=100)
#     picture = models.CharField(max_length=200)
 
#     def __str__(self):
#         return self.name

# class Client(models.Model):
#     name = models.CharField(max_length=50)
#     weight = models.IntegerField()
#     height = models.IntegerField()

#     def __str__(self):
#         return self.name

# class ClientExercise(models.Model):
#     Date = models.DateTimeField(auto_now_add=True)
#     Note = models.CharField(max_length=100)
#     unitAmount = models.CharField(max_length=100)
#     exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
   
class ExerciseTemplate(models.Model):
    name = models.CharField(max_length=50)
    picture = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class ClientExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('2022-22-01')

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    reps = models.IntegerField()
    sets = models.IntegerField()
    time = models.IntegerField()
    note = models.CharField(max_length=100)
    client_exercise = models.ForeignKey(ClientExercise, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
