from django.db import models
from django.contrib.auth.models import User
from django import forms


class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bicep = models.DecimalField(max_digits=5, decimal_places=2)
    forearm = models.DecimalField(max_digits=5, decimal_places=2)
    shoulder = models.DecimalField(max_digits=5, decimal_places=2)
    chest = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    thigh = models.DecimalField(max_digits=5, decimal_places=2)
    calf = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=4, decimal_places=2)
    date_recorded = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'measurements'
