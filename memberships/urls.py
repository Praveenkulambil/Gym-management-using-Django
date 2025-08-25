from django.urls import path
from . import views

urlpatterns = [    
    path('create_plan/', views.create_plan, name='create_plan'),
    path('plan_list/', views.plan_list, name='plan_list'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('payment_list/', views.payment_list, name='payment_list'),
    # path('select_plan/', views.select_plan, name='select_plan'),
    path('payment_list/', views.payment_list, name='payment_list'),
    path('total_active_members/', views.total_active_members, name='total_active_members'),
    path('total_expired_memberships/', views.total_expired_memberships, name='total_expired_memberships'),
    path('payment/<int:user_id>/<int:plan_id>/', views.payment, name='payment'),
    path('success/' , views.success , name='success'),

]
