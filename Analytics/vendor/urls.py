from django.urls import path
from . import views

urlpatterns = [

    path('',views.vendor_loc_data, name='vendor_loc_data'),
]