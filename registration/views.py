from django.http import HttpResponse
from django.shortcuts import  redirect, render
from .forms import RegisterForm, TrainerForm, UserForm
from .models import Registers, Trainers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# @login_required
def register(request):
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
    return render(request, 'registration/add_member.html', {'user_form': user_form, 'member_form': member_form})

@login_required    
def members_list(request):
    members = Registers.objects.all()
    return render(request, 'registration/members_list.html', {'members': members})
def edit_member(request, member_id):
    member = Registers.objects.get(id=member_id) 
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members_list.html')
    else:
        form = RegisterForm(instance=member)
    return render(request, 'registration/edit_member.html', {'form': form})

def delete_member(request, member_id):
    member=Registers.objects.get(id=member_id)
    member.delete()
    return redirect('members_list')

def approve_member(request, member_id):
    member = Registers.objects.get(id=member_id)
    user = member.user
    user.is_active = True
    user.save()
    return redirect('members_list')

def disapprove_member(request, member_id):
    member = Registers.objects.get(id=member_id)
    user = member.user
    user.is_active = False
    user.save()
    return redirect('members_list')

@login_required
def add_trainer(request):
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
            return redirect('trainers_list')
    else:
        user_form = UserForm()
        trainer_form = TrainerForm()
    return render(request, 'registration/add_trainer.html', {'user_form': user_form, 'trainer_form': trainer_form})

@login_required
def trainers_list(request):
    trainers=Trainers.objects.all()
    return render(request,'registration/trainers_list.html',{'trainers':trainers})

def edit_trainer(request, trainer_id):
    trainer = Trainers.objects.get(id=trainer_id) 
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer_id)
        if form.is_valid():
            form.save()
            return redirect('trainers_list')
    else:
        form = RegisterForm(instance=trainer)
    return render(request, 'registration/edit_trainer.html', {'form': form})

def delete_trainer(request, trainer_id):
    trainer=Trainers.objects.get(id=trainer_id)
    trainer.delete()
    return redirect('trainers_list')     


def approve_trainer(request, trainer_id):
    trainer = Trainers.objects.get(id=trainer_id)
    user = trainer.user
    user.is_active = True
    user.save()
    return redirect('trainers_list')

def disapprove_trainer(request, trainer_id):
    trainer = Trainers.objects.get(id=trainer_id)
    user = trainer.user
    user.is_active = False
    user.save()
    return redirect('trainers_list')

def total_members_count(request):
    members_count = User.objects.filter(is_staff=False).count()
    return HttpResponse(f"<script>alert('{members_count}');window.location.replace('/home');</script>")

def total_trainers_count(request):
    trainers_count = User.objects.filter(is_staff=True , is_superuser = False).count()
    return HttpResponse(f"<script>alert('{trainers_count}');window.location.replace('/home');</script>")

def gender_count(request):
    male_count = Registers.objects.filter(sex='Male').count()
    female_count = Registers.objects.filter(sex='Female').count()
    others_count = Registers.objects.filter(sex='Other').count()
    return HttpResponse(f"<script>alert('Total Male : {male_count}, Total Female: {female_count}, Total Gender: {others_count}');window.location.replace('/home');</script>")
