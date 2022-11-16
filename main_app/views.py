from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Exercise, ClientExercise
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import ClientExerciseForm
from datetime import date

import uuid
import boto3


def log(request):
    return render(request, 'logs.html')

def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')
    

def loglist(request, user_id):
    today = date.today()
    today_date = today.strftime("%B %d, %Y")
    clientExercise = ClientExercise.objects.filter (user_id = user_id, date = today ).select_related('exercise')
    exercise = Exercise.objects.exclude (id__in = ClientExercise.objects.filter (user_id = user_id, date = today ).values_list('exercise_id')) 
    return render(request, 'clientExercise/log.html', {'clientExercise': clientExercise, 'today_date': today_date, 'exercise': exercise} )


@login_required
def logAdd (request, user_id, exercise_id):
    form = ClientExerciseForm(request.POST)
    if form.is_valid(): 
      new_ClientExercise = form.save(commit=False)
      new_ClientExercise.date = date.today()    
      new_ClientExercise.user_id = user_id
      new_ClientExercise.exercise_id = exercise_id
      new_ClientExercise.save()
    return redirect('log', user_id = user_id)

    
@login_required  
def ExerciseDelete(request, exercise_id):
  clientExercise = ClientExercise.objects.filter(id = exercise_id)
  clientExercise.delete()
  return redirect('log', user_id = request.user.id)
  new_feeding = form.save(commit=False)


@login_required
def logUpdate(request, clientexercise_id):

  clientExercise = ClientExercise.objects.get(id = clientexercise_id) 
  clientExercise.sets = request.POST['sets']
  
  print (request.POST)
  clientExercise.save()
  print (clientExercise)
  return redirect(f'/clientExercise/{request.user.id}')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('log')
    else:
      error_message = 'Invalid credentials - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def ExerciseDelete(request, exercise_id):
  exercise = Exercise.objects.get(id=exercise_id)
  exercise.delete()
  return reverse('home')

def loglist(request, user_id):
    today = date.today()
    today_date = today.strftime("%B %d, %Y")
    clientExercise = ClientExercise.objects.filter (user_id = user_id ).select_related('exercise')
    exercise = Exercise.objects.exclude (id__in = ClientExercise.objects.filter (user_id = user_id ).values_list('exercise_id'))
    
  
    return render(request, 'clientExercise/log.html', {'clientExercise': clientExercise, 'today_date': today_date, 'exercise': exercise} )



def tracklist(request, user_id):
    clientExercise = ClientExercise.objects.filter (user_id = user_id ).select_related('exercise').order_by('-date')
    print(list(clientExercise))
    exercise = Exercise.objects.exclude (id__in = ClientExercise.objects.filter (user_id = user_id ).values_list('exercise_id')) 
    return render(request, 'clientExercise/track.html', {'clientExercise': clientExercise, 'exercise': exercise} )
# step one: grab all unique dates from back end, pass them down into HTML. Call these 'unique dates'
# step two: Run a for loop in your HTML so that each date in your unique dates list (that you passed down form the backend) is displayed on the page.
# step three: Display the exercise if the date of the exercise matches the date from the list