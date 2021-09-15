from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return HttpResponseRedirect(reverse('customers:create'))

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key
    
    print(user)
    return render(request, 'customers/index.html')

def create(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        street_address = request.POST.get('street_address')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        pickup_day = request.POST.get('pickup_day')
        new_customer = Customer(user=user, first_name=first_name, last_name=last_name, street_address=street_address, state=state, zip_code=zip_code,pickup_day=pickup_day)
        new_customer.save()
        return render(request, 'customers/index.html')
    else:
         return render(request, 'customers/create.html')

def details(request):
    logged_in_customer = Customer.objects.get(user=request.user)

    context = {
        'single_customer': logged_in_customer
    }
    return render(request, 'customers/details.html', context)
