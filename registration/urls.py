from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('members_list/', members_list, name='members_list'),
    path('edit_member/<int:member_id>/', edit_member, name='edit_member'),
    path('delete_member/<int:member_id>/', delete_member, name='delete_member'),
    path('add_trainer/', add_trainer, name='add_trainer'),
    path('trainers_list/', trainers_list, name='trainers_list'),
    path('edit_trainer/<int:trainer_id>/', edit_trainer, name='edit_trainer'),
    path('delete_trainer/<int:trainer_id>/', delete_trainer, name='delete_trainer'),
    path('approve_member/<int:member_id>/', approve_member, name='approve_member'),
    path('disapprove_member/<int:member_id>/', disapprove_member, name='disapprove_member'),
    path('delete_trainer/<int:trainer_id>/', delete_trainer, name='delete_trainer'),
    path('approve_trainer/<int:trainer_id>/', approve_trainer, name='approve_trainer'),
    path('disapprove_trainer/<int:trainer_id>/', disapprove_trainer, name='disapprove_trainer'),
    path('total_members_count/', total_members_count, name='total_members_count'),
    path('total_trainers_count/', total_trainers_count, name='total_trainers_count'),
    path('gender_count/', gender_count, name='gender_count'),
]