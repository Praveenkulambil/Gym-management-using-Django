from django import forms
from .models import Measurements
from django.contrib.auth.models import User

class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ['height', 'weight', 'bicep', 'forearm', 'shoulder', 'chest', 'waist', 'thigh', 'calf', 'bmi', 'date_recorded']
        widgets = {'date_recorded': forms.DateInput(attrs={'type': 'date'})}
