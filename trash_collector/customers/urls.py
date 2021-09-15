from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns
#View for selecting pickup day
#View for requesting extra pickup
#View to suspend account
#

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('details/', views.details, name='details'),
    path('change_pickup/', views.change_pickup, name='change_pickup')
    #Pickup day
    #Suspending service
]
