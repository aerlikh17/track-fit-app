from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    unitType = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    picture = models.CharField(max_length=50)


class Client(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    height = models.IntegerField()



class ClientExercise(models.Model):
    Date = models.DateField('2022-22-01')
    Note = models.CharField(max_length=100)
    unitAmount1 = models.IntegerField()
    unitAmount2 = models.IntegerField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

