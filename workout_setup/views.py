from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WorkoutPlanForm
from .models import WorkoutPlan
from .forms import ExerciseForm
from .models import Exercise



@login_required
def create_workout_plan(request):
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_workout_plan')
    else:
        form = WorkoutPlanForm()
    return render(request, 'workout/create_workout_plan.html', {'form': form})

@login_required
def workout_plan_list(request):
    workout_plans = WorkoutPlan.objects.filter(user=request.user)
    return render(request, 'workout/workout_plan_list.html', {'workout_plans': workout_plans})


def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'workout/exercise_list.html', {'exercises': exercises})

def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExerciseForm()
    return render(request, 'workout/exercise_form.html', {'form': form})