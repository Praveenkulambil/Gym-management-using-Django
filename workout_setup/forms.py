from django import forms
from .models import WorkoutPlan, Exercise
from django.contrib.auth.models import User

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name']


class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['user', 'exercise', 'sets', 'reps', 'day_of_week']

    user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False), label="Select Member")
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all(), label="Select Exercise")
    sets = forms.IntegerField(min_value=1, label="Sets")
    reps = forms.IntegerField(min_value=1, label="Reps")
    day_of_week = forms.ChoiceField(choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ], label="Day of Week")
