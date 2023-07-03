from django.urls import path
from . import views

urlpatterns = [

    path('',views.Artist_Bookings_data, name='Artist_Bookings_data'),
]