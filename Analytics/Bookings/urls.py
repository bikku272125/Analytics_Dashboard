from django.urls import path
from . import views

urlpatterns = [

    path('',views.Artist_Bookings_data, name='Artist_Bookings_data'),
    path('ABdashboard/',views.Artist_Booking_dashboard,name="ABD"),
]