# from django.shortcuts import render
# from requests import request
from django.shortcuts import redirect, render
from requests import request
from .forms import UploadFileForm
import csv
from django.contrib import messages
from django.shortcuts import render
from .models import ArtistBooking
from io import TextIOWrapper
# Create your views here.
# def Bookings_data(request):
#     return render(request , 'Booking.html')

def Artist_Bookings_data(request):
    if request.method == 'POST':
        if 'myfile' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('Artist_Bookings_data')
        
        csv_file = request.FILES['myfile']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Wrong format. Only CSV files are allowed.')
            return redirect('Artist_Bookings_data')
        
        csv_data = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'), delimiter=',')
        
        next(csv_data)  # Skip the header row
        
        for row in csv_data:
            per_day = row[0]
            time = row[1]
            customer_name = row[2]
            gender = row[3]
            artist_name = row[4]
            location = row[5]
            service_name = row[6]
            discount_used = row[7]
            net_amount = row[8]
            status = row[9]
            
            ArtistBooking.objects.create(per_day=per_day,
                                        time=time,
                                        customer_name=customer_name,
                                        gender=gender,
                                        artist_name=artist_name,
                                        location=location,
                                        service_name=service_name,
                                        discount_used=discount_used,
                                        net_amount=net_amount,
                                        status=status
                                        )
        
        messages.success(request, 'Data uploaded successfully')
        return redirect('Artist_Bookings_data')
    
    else:
        ad_data = ArtistBooking.objects.all()
        return render(request, 'Artist Booking.html', {'ad_data': ad_data})

def Booking_data_list(request):
    ad_data = ArtistBooking.objects.all()
    return render(request, 'Artist Booking.html', {'ad_data': ad_data})