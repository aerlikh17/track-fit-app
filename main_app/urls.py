from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('clientExercise/<int:user_id>', views.loglist, name='log'),
  path('clientExercise/add/<int:user_id>/<int:exercise_id>', views.logAdd, name='logAdd'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
  path('exercise/<int:pk>/delete', views.ExerciseDelete, name='exercise-delete'),
  path('clientExercise/track/<int:user_id>', views.tracklist, name='track'),
]