from django.urls import path
from . import views

urlpatterns = [
    
    # path('upload',views.upload, name='upload'),
    path('ad_page/',views.ad_page, name='ad_page'),
    # path('ad_data/',views.ad_data_list,name='delete'),
#     path('delete/',views.ad_data_delete, name='delete')
    path('AdDashboard/',views.AdDashboard,name='AdDashboard'),
    path('delete/', views.delete_rows, name='delete'),
]
