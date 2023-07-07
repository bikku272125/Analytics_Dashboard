from django.urls import path
from . import views

urlpatterns = [

    path('',views.analytics_data, name='analytics_data'),
    path('delete/', views.delete_rows, name='delete'),
    # path('Show/',views.show_view, name='show_view')
    path('ANdashboard/',views.Dash_Analytics, name='Analytics_Dashboard')
]