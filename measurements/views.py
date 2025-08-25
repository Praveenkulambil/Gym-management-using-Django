from django.shortcuts import render, redirect
from .forms import MeasurementsForm
from .models import Measurements
from django.contrib.auth.decorators import login_required

@login_required
def add_measurement(request):
    if request.method == 'POST':
        form = MeasurementsForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user  
            measurement.save()
            return redirect('measurement_list')
    else:
        form = MeasurementsForm()
    return render(request, 'measurements/add_measurement.html', {'form': form})

@login_required
def measurement_list(request):
    measurements = Measurements.objects.filter(user=request.user)
    return render(request, 'measurements/measurement_list.html', {'measurements': measurements})
