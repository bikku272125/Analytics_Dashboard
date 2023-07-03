from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UploadFileForm

# Create your views here.
import csv
from django.contrib import messages
from django.shortcuts import render
from .models import DailyStats
from io import TextIOWrapper
from django.db.models import Count
import pandas as pd
from django.core.paginator import Paginator

def ad_page(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')

        if not csv_file:
            messages.error(request, 'No file uploaded.')
            return redirect('ad_page')

        # if not csv_file:
        #     messages.error(request, 'No file uploaded.')
        #     return redirect('ad_page')
        csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
        next(csv_data)  #skip the header row

        for row in csv_data:
            date = row[0]
            clicks = row[1]
            cost = row[2]
            conversions = row[3]
            cost_per_conversion = row[4]
            search_word = row[5]
            search_word_clicks = row[6]
            search_word_impressions = row[7]
            search_word_cost = row[8]
            search_salon = row[9]
            search_salon_clicks = row[10]
            search_salon_impressions = row[11]
            search_salon_cost = row[12]
            search_keyword = row[13]
            search_keyword_clicks = row[14]
            search_keyword_ctr = row[15]
            campaign_name = row[16]
            optimization_score = row[17]
            network_name = row[18]
            network_clicks = row[19]
            network_cost = row[20]
            device_name = row[21]
            device_cost = row[22]
            device_clicks = row[23]
            device_conversion = row[24]
            gender = row[25]
            age_range = row[26]
            gender_impression = row[27]
            per_hour = row[28]
            per_hour_impression = row[29]
            per_day = row[30]
            per_day_per_hour = row[31]
            per_day_per_hour_impression = row[32]
            campaigns_cost = row[33]
            campaigns_conversion = row[34]
            campaigns_cost_per_conversion = row[35]

            DailyStats.objects.create(
                date=date,
                clicks=clicks,
                cost=cost,
                conversions=conversions,
                cost_per_conversion=cost_per_conversion,
                search_word=search_word,
                search_word_clicks=search_word_clicks,
                search_word_impressions=search_word_impressions,
                search_word_cost=search_word_cost,
                search_salon=search_salon,
                search_salon_clicks=search_salon_clicks,
                search_salon_impressions=search_salon_impressions,
                search_salon_cost=search_salon_cost,
                search_keyword=search_keyword,
                search_keyword_clicks=search_keyword_clicks,
                search_keyword_ctr=search_keyword_ctr,
                campaign_name=campaign_name,
                optimization_score=optimization_score,
                network_name=network_name,
                network_clicks=network_clicks,
                network_cost=network_cost,
                device_name=device_name,
                device_cost=device_cost,
                device_clicks=device_clicks,
                device_conversion=device_conversion,
                gender=gender,
                age_range=age_range,
                gender_impression=gender_impression,
                per_hour=per_hour,
                per_hour_impression=per_hour_impression,
                per_day=per_day,
                per_day_per_hour=per_day_per_hour,
                per_day_per_hour_impression=per_day_per_hour_impression,
                campaigns_cost=campaigns_cost,
                campaigns_conversion=campaigns_conversion,
                campaigns_cost_per_conversion=campaigns_cost_per_conversion
            )

        messages.success(request, 'Data uploaded successfully')
        return redirect('ad_page')
    
    else:
        ad_data = DailyStats.objects.all()
        # paginator = Paginator(ad_data , 10)   # Display 10 rows
        # page_number = request.GET.get('ad_page')
        # page_obj = paginator.get_page(page_number)
        # return render(request, 'ad_page.html',{'page_obj': page_obj})
        return render(request, 'ad_page.html', {'ad_data': ad_data})



def delete_rows(request):
    if request.method == 'POST':
        selected_ids = request.GET.get('ids').split(',')
        DailyStats.objects.filter(id__in=selected_ids).delete()
    
    return redirect('ad_page')
# def ad_data_list(request):
#     ad_data = DailyStats.objects.all()
#     return render(request, 'ad_page.html', {'ad_data': ad_data})
# def dash(request):
#     data_count = DailyStats.objects.count()
#     print("Data Count:", data_count)
#     return render(request, 'dashboard.html', {'data_count': data_count})
from django.db.models import Sum, Avg

def AdDashboard(request):
    
    total_click = DailyStats.objects.aggregate(total_click=Sum('clicks'))
    total_cost = DailyStats.objects.aggregate(total_cost=Sum('cost'))
    total_conversion = DailyStats.objects.aggregate(total_conversion=Sum('conversions'))
    total_cpc = DailyStats.objects.aggregate(total_cpc=Avg('cost_per_conversion'))
    data = DailyStats.objects.all().values('date', 'clicks', 'conversions', 'cost_per_conversion')
    chart_data = list(data)
    
    chart_dates = [datetime.strptime(entry['date'], '%a, %d %b %Y').date() for entry in chart_data if entry['date']]

    return render(request, 'Adword_Dashboard.html', {
        'total_click': total_click,
        'total_cost': total_cost,
        'total_conversion': total_conversion,
        'total_cpc': total_cpc,
        'chart_data': chart_data,
        'chart_dates': chart_dates
        
    })
    
    
# def AdDashboard(request):
#     # Fetch the data from the DailyStats model
#     data = DailyStats.objects.exclude(date='').order_by('date')

#     # Prepare the data for the line chart
#     dates = []
#     clicks = []
#     cost = []
#     conversions = []

#     for entry in data:
#         # Skip entries where date field is empty
#         if not entry.date:
#             continue

#         # Convert the date string to a datetime object
#         try:
#             date = datetime.strptime(entry.date, '%a-%d-%m-%Y')
#         except ValueError:
#             # Handle invalid date format if necessary
#             continue

#         dates.append(date)
#         clicks.append(int(entry.clicks))
#         cost.append(float(entry.cost))
#         conversions.append(int(entry.conversions))

#     context = {
#         'dates': dates,
#         'clicks': clicks,
#         'cost': cost,
#         'conversions': conversions,
#     }

#     return render(request, 'Adword_Dashboard.html', context)


def ad_page(request):
    # Fetch all ad_data objects
    all_ad_data = DailyStats.objects.all()

    # Set the number of items per page
    items_per_page = 10

    # Create a Paginator object
    paginator = Paginator(all_ad_data, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page = paginator.get_page(page_number)

    return render(request, 'ad_page.html', {'ad_data': page})


