from django.http import HttpResponse
from .forms import PlanForm, PaymentForm,PlanSelectionForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Plan, Payment
from dateutil.relativedelta import relativedelta
from django.utils import timezone

@login_required
def create_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plan_list')
    else:
        form = PlanForm()
    return render(request, 'memberships/create_plan.html', {'form': form})

@login_required
def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'memberships/plan_list.html', {'plans': plans})

@login_required
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PaymentForm()
    return render(request, 'memberships/create_payment.html', {'form': form})

# @login_required
# def select_plan(request):
#     if request.method == 'POST':
#         form = PlanSelectionForm(request.POST)
#         if form.is_valid():
#             payment = form.save(commit=False)
#             payment.amount = payment.plan.price
#             if not payment.expiry_date:
#                 payment.expiry_date = payment.start_date + relativedelta(months=payment.plan.duration)
#             payment.save()
#             return redirect('home')
#     else:
#         form = PlanSelectionForm()
#     return render(request, 'memberships/select_plan.html', {'form': form})

@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'memberships/payment_list.html', {'payments': payments})

@login_required
def total_active_members(request):
    today = timezone.now().date()
    active_members_count = Payment.objects.filter(expiry_date__gte=today).count()
    return HttpResponse(f"<script>alert('Total Active Members: {active_members_count}');window.location.replace('/home');</script>")

@login_required
def total_expired_memberships(request):
    today = timezone.now().date()
    expired_memberships_count = Payment.objects.filter(expiry_date__lt=today).count()
    return HttpResponse(f"<script>alert('Total Expired Memberships: {expired_memberships_count}');window.location.replace('/home');</script>")

import razorpay
from django.views.decorators.csrf import csrf_exempt  

def payment(request,user_id,plan_id):
    try:
        x = Payment.objects.get(user_id=user_id, plan_id=plan_id)
    except Payment.DoesNotExist:
        return render(request, 'memberships/error.html', {"msg": "No such payment exists."})
    
    if request.method == "POST":
        # for i in x: 
        print("Amount:", x.amount)
        amount=int(x.amount)*100
        client = razorpay.Client(auth =("rzp_test_ifqXZb84qSL1CP" , "IwSyyaBvXh300nlqM0kqb0ow"))
        payment = client.order.create({'amount':amount, 'currency':'INR','payment_capture':'1' })
        first_payment = x
        first_payment.razorpay_order_id = payment['id']
        first_payment.save()
        return render(request, 'memberships/razorpay.html' ,{'payment':payment})
    print(user_id,plan_id)
    print(x)
    # for i in x:
    name = x.user.username
    email = x.user.email
    amount =int(x.amount)*100
    return render(request, 'memberships/razorpay.html',{"name":name,"email":email,"amount":amount})

@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        print(a)
        order_id = a.get("razorpay_order_id")
        print("Order ID:", order_id)

        if order_id:
            try:
                payment = Payment.objects.get(razorpay_order_id=order_id)
                payment.status = "paid"
                payment.save()
                print("Payment marked as paid for user:", payment.user.username)
            except Payment.DoesNotExist:
                print("No matching payment found for this Razorpay order ID.")
        order_id = ""
        for key , val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        return redirect('payment_list')
    return render(request, "memberships/success.html")









