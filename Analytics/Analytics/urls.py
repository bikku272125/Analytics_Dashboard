
from django.contrib import admin
from django.urls import path,include
from vendor.views import VLD
from Bookings.views import Artist_Booking_dashboard
from gadwords.views import delete_rows
from ganalytics.views import Dash_Analytics
from Artist.views import Artist_loc_dash
from Bookings_vendor.views import vnd_dashboard
from gadwords.views import ad_page
from Meta.views import meta_data
from ganalytics.views import analytics_data
from Bookings.views import Artist_Bookings_data




from Dashboard.views import login_view,dashboard_view,logout_view,ad_data_list,date
from gadwords import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('gadwords.urls')),
    # path("upload/",include('gadwords.urls')),
    path("meta/",include('Meta.urls')),
    path("analytics/",include('ganalytics.urls')),
    path("ArtistBookings/",include('Bookings.urls')),
     path('BKvendor/',include('Bookings_vendor.urls')),
    path('location_Artist',include('Artist.urls')),
    path('location_vendor/',include('vendor.urls')),
    # path('list/',ad_data_list,name='list'),
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    # path('dash/',date, name='data_count'),
    path('Artist_Location_dashboard/', Artist_loc_dash,name="Artist_location_dashboard"),
    path('delete',delete_rows,name='delete'),
    path('VBdashboard/',vnd_dashboard, name='vendor_Booking_Dashboard'),
    path('ANdashboard/',Dash_Analytics, name='Analytics_Dashboard'),
    
    path('ABdashboard/',Artist_Booking_dashboard,name="ABD"),
     path('VL_dashboard/',VLD, name='VLD'),
    
]
