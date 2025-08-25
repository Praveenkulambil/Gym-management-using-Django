from django.urls import path
from . import views

urlpatterns = [
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance_stats/', views.attendance_stats, name='attendance_stats'),
    path('attendance_totalstats/', views.attendance_totalstats, name='attendance_totalstats'),
    path('attendance_totalstats_today/', views.attendance_totalstats_today, name='attendance_totalstats_today'),
        path('select_plan/', views.select_plan, name='select_plan'),

]
