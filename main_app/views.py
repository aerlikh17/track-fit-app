from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Exercise, ClientExercise
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3


def log(request):
    return render(request, 'logs.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def loglist(request, user_id):
    today = date.today()
    today_date = today.strftime("%B %d, %Y")
    clientExercise = ClientExercise.objects.filter (user_id = user_id ).select_related('exercise')
    exercise = Exercise.objects.exclude (id__in = ClientExercise.objects.filter (user_id = user_id ).values_list('exercise_id'))
    
  
    return render(request, 'clientExercise/log.html', {'clientExercise': clientExercise, 'today_date': today_date, 'exercise': exercise} )


