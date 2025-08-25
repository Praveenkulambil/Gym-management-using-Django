from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in months")

    def __str__(self):
        return self.name

STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('paid', 'Paid'),
)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        unique_together = ('user', 'plan') 

    def __str__(self):
        return f'{self.user.username} - {self.plan.name}'

    def save(self, *args, **kwargs):
        if not self.expiry_date:
            self.expiry_date = self.start_date + relativedelta(months=self.plan.duration)
        super().save(*args, **kwargs)
