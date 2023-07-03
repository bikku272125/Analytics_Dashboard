# from django.shortcuts import render
# from requests import request
# # Create your views here.
# def Artist_data(request):
#     return render(request , 'artist.html')
from django.shortcuts import redirect, render
from requests import request
from .forms import UploadFileForm
import csv
from django.contrib import messages
from django.shortcuts import render
from .models import Artist
from io import TextIOWrapper

def Artist_data(request):
    if request.method == 'POST':
        if 'myfile' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('Artist_data')
        
        csv_file = request.FILES['myfile']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Wrong format. Only CSV files are allowed.')
            return redirect('Artist_data')
        
        csv_data = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'), delimiter=',')
        
        next(csv_data)  # Skip the header row
        
        for row in csv_data:
            name = row[0]
            location = row[1]
            latitude = row[2]
            longitude = row[3]
            is_active = row[4].lower() == 'true'  # Convert string to boolean
            is_inactive = row[5].lower() == 'true'  # Convert string to boolean
            
            Artist.objects.create(name=name, location=location, latitude=latitude, longitude=longitude, is_active=is_active, is_inactive=is_inactive)
        
        messages.success(request, 'Data uploaded successfully')
        return redirect('Artist_data')
    
    else:
        ad_data = Artist.objects.all()
        return render(request, 'artist_location.html', {'ad_data': ad_data})

def Artist_data_list(request):
    ad_data = Artist.objects.all()
    return render(request, 'artist_location.html', {'ad_data': ad_data})

def Artist_loc_dash(request):
    return render(request,"Artist_location_Dashboard.html")