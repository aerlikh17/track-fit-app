from django.urls import path, include
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('clientExercise/<int:client_id>', views.loglist, name='log'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
]