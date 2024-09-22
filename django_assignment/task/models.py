from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.shortcuts import render

class Order(models.Model):
    customer = models.CharField(max_length=100)
    order_date = models.DateField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def top_customers(last_n_months=6):
        six_months_ago = timezone.now() - timezone.timedelta(days=last_n_months*30)
        return Order.objects.filter(order_date__gte=six_months_ago) \
                   .values('customer') \
                   .annotate(total_spent=Sum('total_amount')) \
                   .order_by('-total_spent')[:5]
