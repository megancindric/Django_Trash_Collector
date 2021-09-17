from .models import Employee
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.apps import apps
from datetime import date
import calendar

# Create your views here.

#Displays pickupsf for:
    #Customers in employee zip code, where pickup day is today & service is not suspended OR there is a 1-time pickup scheduled for today
def index(request):
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_employee = Employee.objects.get(user=user)
    except:
        return HttpResponseRedirect(reverse('employees:create'))

    Customer = apps.get_model('customers.Customer')
    all_customers = Customer.objects.all()
    matching_customers = []
    today = date.today()
    today_string = calendar.day_name[today.weekday()]
    for customer in all_customers:
        is_suspended = customer.suspension_start < today and customer.suspension_end > today
        if customer.has_extra_pickup and customer.extra_pickup_day == today:
            matching_customers.append(customer)
        elif customer.pickup_day == today_string and not is_suspended:
            matching_customers.append(customer)
    context = {
        'matching_customers': matching_customers
    }
    print(user)
    print(matching_customers)
    return render(request, 'employees/index.html', context)

#Display all ccustomers in zip code, option to filter by pickup day
def my_accounts(request):
    user = request.user
    logged_in_employee = Employee.objects.get(user=user)
    Customer = apps.get_model('customers.Customer')
    matching_customers = []
    
    if(request.method == "POST" and request.POST.get("pickup_day") != "All"):
        pickup_day = request.POST.get("pickup_day")
        all_customers = Customer.objects.filter(pickup_day=pickup_day)
    else:
        all_customers = Customer.objects.all()

    for customer in all_customers:
        if customer.zip_code == logged_in_employee.zip_code:
            matching_customers.append(customer)
    
    context = {
        'matching_customers': matching_customers
    }

    return render(request, 'employees/my_accounts.html', context)

def create(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        zip_code = request.POST.get('zip_code')
        new_customer = Employee(user=user, first_name=first_name, last_name=last_name, zip_code=zip_code)
        new_customer.save()
        return render(request, 'employees/index.html')
    else:
         return render(request, 'employees/create.html')

def confirm_pickup(request):
    pass
#TODO - will select current customer, ask to confirm pickup, then on click will charge customer