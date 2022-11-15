from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('/', views.home, name='home'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
  path('logs/', views.log, name='logs'),
  path('exercise/<int:pk>/delete', views.ExerciseDelete, name='exercise-delete'),
]