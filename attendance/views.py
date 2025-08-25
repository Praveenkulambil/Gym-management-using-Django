from datetime import datetime, date
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AttendanceRecord
from .forms import AttendanceForm
from django.utils import timezone
from memberships.forms import PlanSelectionForm
from dateutil.relativedelta import relativedelta

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('attendance_stats')
    else:
        form = AttendanceForm(user=request.user)
    return render(request, 'attendance/mark_attendance.html', {'form': form})

@login_required
def attendance_stats(request):
    user = request.user
    records = AttendanceRecord.objects.filter(user=user)
    return render(request, 'attendance/attendance_stats.html', {'records': records})

@login_required
def attendance_totalstats_today(request):
    today = date.today()
    records = AttendanceRecord.objects.filter(date=today)
    count = records.count() 
    return HttpResponse(f"<script>alert('{count}');window.location.replace('/home');</script>")


def attendance_totalstats(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    records = AttendanceRecord.objects.filter(date__month=current_month, date__year=current_year)
    count = records.count() 
    return HttpResponse(f"<script>alert('{count}');window.location.replace('/home');</script>")


# @login_required
# def select_plan(request):
#     if request.method == 'POST':
#         form = PlanSelectionForm(request.POST)
#         if form.is_valid():
#             payment = form.save(commit=False)
#             print(request.user)
#             payment.user = request.user 
#             payment.amount = payment.plan.price
#             if not payment.expiry_date:
#                 payment.expiry_date = payment.start_date + relativedelta(months=payment.plan.duration)
#             payment.save()
#             return redirect('home')
#     else:
#         form = PlanSelectionForm()
#     return render(request, 'memberships/select_plan.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from dateutil.relativedelta import relativedelta


@login_required
def select_plan(request):
    if request.method == 'POST':
        form = PlanSelectionForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user 
            payment.amount = payment.plan.price
            if not payment.expiry_date:
                payment.expiry_date = payment.start_date + relativedelta(months=payment.plan.duration)
            try:
                payment.save()
                messages.success(request, "Plan selected successfully!")
                return redirect('home')
            except IntegrityError:
                messages.error(request, "You have already selected this plan.")
    else:
        form = PlanSelectionForm()
    return render(request, 'memberships/select_plan.html', {'form': form})
