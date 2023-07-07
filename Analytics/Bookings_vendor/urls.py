from django.urls import path
from . import views

urlpatterns = [

    path('',views.Vendor_Booking_Data, name='Booking_vendor'),
   path('VBdashboard/',views.vnd_dashboard, name='vendor_Booking_Dashboard'),
]