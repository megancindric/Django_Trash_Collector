from .models import Employee
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.apps import apps
from datetime import date
import calendar

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.
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
        #Today's date needs to be > start and <
            matching_customers.append(customer)

        #filter(zip_code=logged_in_employee.zip_code)
        #Matches our zip
        #Today is customer's pickup day
        #Customer is not suspended
        #Today is customer's 1-time pickup
    context = {
        'matching_customers': matching_customers
    }
    print(user)
    print(matching_customers)
    return render(request, 'employees/index.html', context)

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
