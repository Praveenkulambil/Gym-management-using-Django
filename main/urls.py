from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index', index, name='index'),
    path('', main, name='main'),
    path('home', home, name='home'),
    path('member_register', member_register, name='member_register'),
    path('trainer_register', trainer_register, name='trainer_register'),
    path('login_view', login_view, name='login_view'),
    path('logout',logouts,name="logout"),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]