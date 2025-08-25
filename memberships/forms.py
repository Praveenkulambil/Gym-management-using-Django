from django import forms
from .models import Plan, Payment
from django.contrib.auth.models import User
from .models import Plan, Payment

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'description', 'price', 'duration']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'plan', 'amount', 'expiry_date']

class PlanSelectionForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False), label="Select Member")
    start_date = forms.DateField(widget=forms.SelectDateWidget)
    expiry_date = forms.DateField(widget=forms.SelectDateWidget, required=False)

    class Meta:
        model = Payment
        fields = [ 'plan', 'start_date', 'expiry_date']
