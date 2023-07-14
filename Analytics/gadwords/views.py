from datetime import date, datetime
from django.http import HttpResponse, JsonResponse
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
from django.template import loader

def ad_page(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')

        if not csv_file:
            messages.error(request, 'No file uploaded.')
            return redirect('ad_page')

        csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
        next(csv_data)  # Skip the header row

        for row in csv_data:
            # Assuming the CSV columns follow the order you specified
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
        all_ad_data = DailyStats.objects.all().order_by('id')

        # Set the number of items per page
        items_per_page = 10

        # Create a Paginator object
        paginator = Paginator(all_ad_data, items_per_page)

        # Get the current page number from the request's GET parameters
        page_number = request.GET.get('page')

        # Get the Page object for the requested page number
        page = paginator.get_page(page_number)

        return render(request, 'ad_page.html', {'ad_data': page})

def ad_data_list(request):
    ad_data = DailyStats.objects.all()
    return render(request, 'ad_page.html', {'ad_data': ad_data})

def delete_rows(request):
    if request.method == 'POST':
        selected_ids = request.GET.get('ids').split(',')
        DailyStats.objects.filter(id__in=selected_ids).delete()
    
    return redirect('ad_page')

# def dash(request):
#     data_count = DailyStats.objects.count()
#     print("Data Count:", data_count)
#     return render(request, 'dashboard.html', {'data_count': data_count})
from django.db.models import Sum, Avg

# def AdDashboard(request):
    
#     # total_click = DailyStats.objects.aggregate(total_click=Sum('clicks'))
#     # total_cost = DailyStats.objects.aggregate(total_cost=Sum('cost'))
#     # total_conversion = DailyStats.objects.aggregate(total_conversion=Sum('conversions'))
#     # total_cpc = DailyStats.objects.aggregate(total_cpc=Avg('cost_per_conversion'))
#     # data = DailyStats.objects.all().values('date', 'clicks', 'conversions', 'cost_per_conversion')
#     # chart_data = list(data)
#     data = DailyStats.objects.all()
#     context = {
#         'data' : data,
#     }
#     # chart_dates = [datetime.strptime(entry['date'], '%a, %d %b %Y').date() for entry in chart_data if entry['date']]

#     return render(request, 'Adword_Dashboard.html',context)
#         # 'total_click': total_click,
#         # 'total_cost': total_cost,
#         # 'total_conversion': total_conversion,
#         # 'total_cpc': total_cpc,
#         # 'chart_data': chart_data,
#         # 'chart_dates': chart_dates,
#     #     'data': data
            
        
#     # })
# def AdDashboard(request):
#     total_click = DailyStats.objects.aggregate(total_click=Sum('clicks'))
#     total_cost = DailyStats.objects.aggregate(total_cost=Sum('cost'))
#     total_conversion = DailyStats.objects.aggregate(total_conversion=Sum('conversions'))
#     total_cpc = DailyStats.objects.aggregate(total_cpc=Avg('cost_per_conversion'))

#     data = DailyStats.objects.all()
#     context = {
#         'data': data,
#         'total_click': total_click['total_click'],
#         'total_cost': total_cost['total_cost'],
#         'total_conversion': total_conversion['total_conversion'],
#         'total_cpc': total_cpc['total_cpc']
#     }

#     return render(request, 'Adword_Dashboard.html', context)


# def ad_page(request):
#     # Fetch all ad_data objects
#     all_ad_data = DailyStats.objects.all()

#     # Set the number of items per page
#     items_per_page = 10

#     # Create a Paginator object
#     paginator = Paginator(all_ad_data, items_per_page)

#     # Get the current page number from the request's GET parameters
#     page_number = request.GET.get('page')

#     # Get the Page object for the requested page number
#     page = paginator.get_page(page_number)

#     return render(request, 'ad_page.html', {'ad_data': page})

# def AdDashboard(request):
#     data = DailyStats.objects.all()

#     total_click = None
#     total_cost = None
#     total_conversion = None
#     total_cpc = None

#     if data:
#         total_click = DailyStats.objects.aggregate(total_click=Sum('clicks'))
#         total_cost = DailyStats.objects.aggregate(total_cost=Sum('cost'))
#         total_conversion = DailyStats.objects.aggregate(total_conversion=Sum('conversions'))
#         total_cpc = DailyStats.objects.aggregate(total_cpc=Avg('cost_per_conversion'))

#     context = {
#         'data': data,
#         'total_click': total_click['total_click'] if total_click else None,
#         'total_cost': total_cost['total_cost'] if total_cost else None,
#         'total_conversion': total_conversion['total_conversion'] if total_conversion else None,
#         'total_cpc': total_cpc['total_cpc'] if total_cpc else None
#     }

#     return render(request, 'Adword_Dashboard.html', context)

def testing(request):
    data = DailyStats.objects.all()
    count = DailyStats.objects.all()
    clicks = DailyStats.objects.all()
    cost = DailyStats.objects.all()
    search_word = DailyStats.objects.all()
    cpc = DailyStats.objects.all()
    template = loader.get_template('Adword_Dashboard.html')
    
    context = {
        'count': count,
        'data':data[:30],
        'clicks':clicks,
        'cost' : cost,
        'search_word':search_word,
        'cost_per_conversion':cpc,
        'search_word': search_word,
        
    }
    return HttpResponse(template.render(context,request))
 
 
 
 

