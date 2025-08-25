from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import  redirect, render
from django.http import HttpResponse
from registration.forms import RegisterForm, TrainerForm, UserForm
from registration.models import Registers, Trainers
def index(request):
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')

def member_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        member_form = RegisterForm(request.POST)
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.is_active = False
            user.save()
            student = member_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('login_view')
    else:
        user_form = UserForm()
        member_form = RegisterForm()
    return render(request, 'member_register.html', {'user_form': user_form, 'member_form': member_form})

def trainer_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        trainer_form = TrainerForm(request.POST)
        if user_form.is_valid() and trainer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.is_active = False
            user.is_staff = True
            user.save()
            trainer = trainer_form.save(commit=False)
            trainer.user = user
            trainer.save()
            return redirect('login_view')
    else:
        user_form = UserForm()
        trainer_form = TrainerForm()
    return render(request, 'trainer_register.html', {'user_form': user_form, 'trainer_form': trainer_form})


@login_required
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home') 
            else:
                return HttpResponse("<script>alert('Your account is inactive.');window.location.href='/';</script>")
        else:
             return HttpResponse("<script>alert('Invalid login details.');window.location.href='/';</script>")
    return render(request, 'login.html')



def logouts(request):
    logout(request)
    return redirect(login_view)