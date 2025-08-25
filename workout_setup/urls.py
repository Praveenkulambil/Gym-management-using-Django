# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create_workout_plan/', views.create_workout_plan, name='create_workout_plan'),
    path('workout_plan_list/', views.workout_plan_list, name='workout_plan_list'),
    path('exercise_list/', views.exercise_list, name='exercise_list'),
    path('exercise_create/', views.exercise_create, name='exercise_create'),
]
