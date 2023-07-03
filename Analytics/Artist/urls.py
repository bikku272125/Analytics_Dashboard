from django.urls import path
from . import views

urlpatterns = [

    path('',views.Artist_data, name='Artist_data'),
    path('dash',views.Artist_loc_dash,name=('Artist_location_dashboard'))
]