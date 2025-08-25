from django import forms
from .models import AttendanceRecord
from django.utils import timezone

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ['user', 'date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AttendanceForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user
            self.fields['user'].disabled = True
        self.fields['date'].initial = timezone.now().date()
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
