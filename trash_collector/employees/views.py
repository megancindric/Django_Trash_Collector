from .models import Employee
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.apps import apps

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.
def index(request):
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_employee = Employee.objects.get(user=user)
        Customer = apps.get_model('customers.Customer')
        #Matches our zip
        #Today is customer's pickup day
        #Customer is not suspended
        #Today is customer's 1-time pickup

    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return HttpResponseRedirect(reverse('employees:create'))

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key
    
    print(user)
    return render(request, 'employees/index.html')

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
