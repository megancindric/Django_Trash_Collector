from django.db import models
import datetime
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories
#TODO: Add custom constants for state, pickup day

class Customer(models.Model):
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    zip_code = models.IntegerField()
    pickup_day = models.CharField(max_length=9)
    has_extra_pickup = models.BooleanField(default=False)
    extra_pickup_day = models.DateField(default=datetime.datetime(2000, 1, 1)) #Defaulte date as 1/1/2000
    is_suspended = models.BooleanField(default=False)
    suspension_start = models.DateField(default=datetime.datetime(2000, 1, 1)) #Defaulte date as 1/1/2000
    suspension_end = models.DateField(default=datetime.datetime(2000, 1, 1)) #Defaulte date as 1/1/2000
    current_balance = models.DecimalField(decimal_places = 2, default=0.00, max_digits=5)
