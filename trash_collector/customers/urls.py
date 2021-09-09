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
    path('register/', views.create, name='create'),
    #Pickup day
    #Suspending service
]
