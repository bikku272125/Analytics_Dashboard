# from django.shortcuts import render
# from requests import request
from django.shortcuts import redirect, render
from requests import request
from .forms import UploadFileForm
import csv
from django.contrib import messages
from django.shortcuts import render
from .models import VendorBooking
from io import TextIOWrapper
from datetime import datetime
# Create your views here.
# def Bookings_data(request):
#     return render(request , 'Booking.html')

def Vendor_Booking_Data(request):
    if request.method == 'POST':
        if 'myfile' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('Booking_vendor')
        
        csv_file = request.FILES['myfile']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Wrong format. Only CSV files are allowed.')
            return redirect('Booking_vendor')
        
        csv_data = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'), delimiter=',')
        
        next(csv_data) # Skip the header row
        
        for row in csv_data:
            vendor_name = row[0]
            booking_date = row[1]
            service_gender = row[2]
            service_customer_name = row[3]
            promotional_code = row[4]
            promotional_code_count = row[5]
            promotional_code_amount = row[6]
            cancel_booking = row[7]
            complete_booking = row[8]
            pending_booking = row[9]
            
            try:
                booking_date = datetime.strptime(booking_date, '%Y/%m/%d').strftime('%Y-%m-%d')
            except ValueError:
                messages.error(request, f'Invalid date format: {booking_date}. Use the format "YYYY/MM/DD".')
                return redirect('Booking_vendor')
               
            VendorBooking.objects.create(
                vendor_name=vendor_name,
                booking_date=booking_date,
                service_gender=service_gender,
                service_customer_name=service_customer_name,
                promotional_code=promotional_code,
                promotional_code_count=promotional_code_count,
                promotional_code_amount=promotional_code_amount,
                cancel_booking=cancel_booking,
                complete_booking=complete_booking,
                pending_booking=pending_booking 
            )
                                         
        messages.success(request, 'Data uploaded successfully')
        return redirect('Booking_vendor')
    else:
        ad_data = VendorBooking.objects.all()
        return render(request, 'vendor_Booking.html', {'ad_data': ad_data})


def Booking_data_list(request):
    ad_data = VendorBooking.objects.all()
    return render(request, 'vendor_Booking.html', {'ad_data': ad_data})

def vnd_dashboard(request):
    return render(request, 'vendor_Dashboard.html')