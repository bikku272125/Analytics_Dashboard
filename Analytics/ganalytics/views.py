
from datetime import datetime
from django.shortcuts import redirect, render
from django.views import View
from .forms import UploadFileForm

# Create your views here.
import csv
from django.contrib import messages
from django.shortcuts import render
from .models import Analytics
from io import TextIOWrapper
from django.core.paginator import Paginator


def analytics_data(request):
    if request.method == 'POST':
        if 'myfile' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('analytics_data')
        
        csv_file = request.FILES['myfile']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Wrong format. Only CSV files are allowed.')
            return redirect('analytics_data')
        
        csv_data = csv.reader(TextIOWrapper(csv_file, encoding='utf-8'), delimiter=',')
        
        next(csv_data)  # Skip the header row
        
        for row in csv_data:
            default_channel_grouping = row[0]
            default_sessions = row[1]
            default_new_users = row[2] 
            browser = row[3]
            browser_users = row[4] 
            browser_new_users = row[5] 
            browser_sessions = row[6]  
            browser_bounce_rate = row[7] 
            browser_pages_session = row[8] 
            day_index = row[9]
            day_users = row[10]
            day_sessions = row[11]
            day_benchmark_sessions = row[12]
            device_category = row[13]
            device_sessions_benchmark_delta=row[14] 
            device_sessions = row[15] 
            device_benchmark_sessions = row[16]
            device_new_sessions_benchmark_delta = row[17] 
            device_new_sessions = row[18] 
            device_benchmark_new_sessions = row[19] 
            device_new_users_benchmark_delta = row[20]
            # device_new_users = row[21]
            device_benchmark_new_users = row[21]
            device_pages_session_benchmark_delta = row[22] 
            device_pages_session = row[23] 
            device_benchmark_pages_session = row[24] 
            device_avg_session_duration = row[25] 
            device_avg_benchmark_session_duration = row[26] 
            device_bounce_rate_benchmark_delta = row[27] 
            device_bounce_rate = row[28] 
            device_benchmark_bounce_rate = row[29] 
            device_impressions = row[30] 
            device_clicks = row[31] 
            device_ctr = row[32] 
            device_average_position = row[33] 
            device_2_sessions = row[34] 
            device_2_bounce_rate = row[35] 
            mobile_device_info = row[36]
            mobile_users = row[37]   
            mobile_new_users = row[38] 
            campaign_campaign_id = row[39]
            campaign_clicks = row[40]   
            campaign_cost = row[41]  
            campaign_cpc = row[42]   
            display_keywords = row[43]
            display_campaign = row[44]
            display_google_ads_ad_group = row[45]
            display_clicks = row[46] 
            display_cost = row[47] 
            display_cpc = row[48] 
            final_url = row[49]
            final_clicks = row[50] 
            final_cost = row[51]  
            final_cpc = row[52]  
            keyword = row[53]
            keyword_clicks = row[54] 
            keyword_cost = row[55] 
            keyword_cpc = row[56] 
            affinity_category_reach = row[57]
            affinity_users = row[58] 
            landing_page = row[59]
            landing_impressions = row[60] 
            landing_clicks = row[61] 
            landing_ctr = row[62] 
            country = row[63]
            country_users = row[64]
            country_new_users = row[65]
            page_views = row[66]
            unique_page_views = row[67]
            search_query = row[68]
            search_query_clicks = row[69] 
            search_query_impressions = row[70]
            search_query_ctr = row[71] 
            search_query_avg_position = row[72] 
            source = row[73]
            source_users = row[74]
            # source_new_users = row[75]
            
            # day_index = datetime.strptime(row[9], '%d/%m/%Y').date()

            Analytics.objects.create(
                default_channel_grouping=default_channel_grouping,
                default_sessions=default_sessions,
                default_new_users=default_new_users,
                browser=browser,
                browser_users=browser_users,
                browser_new_users=browser_new_users,
                browser_sessions=browser_sessions,
                browser_bounce_rate=browser_bounce_rate,
                browser_pages_session=browser_pages_session,
                day_index=day_index,
                day_users=day_users,
                day_sessions=day_sessions,
                day_benchmark_sessions=day_benchmark_sessions,
                device_category=device_category,
                device_sessions_benchmark_delta=device_sessions_benchmark_delta,
                device_sessions=device_sessions,
                device_benchmark_sessions=device_benchmark_sessions,
                device_new_sessions_benchmark_delta=device_new_sessions_benchmark_delta,
                device_new_sessions =  device_new_sessions,
                device_benchmark_new_sessions=device_benchmark_new_sessions,
                device_new_users_benchmark_delta=device_new_users_benchmark_delta,
                device_benchmark_new_users=device_benchmark_new_users,
                device_pages_session_benchmark_delta=device_pages_session_benchmark_delta,
                device_pages_session=device_pages_session,
                device_benchmark_pages_session=device_benchmark_pages_session,
                device_avg_session_duration=device_avg_session_duration,
                device_avg_benchmark_session_duration=device_avg_benchmark_session_duration,
                device_bounce_rate_benchmark_delta=device_bounce_rate_benchmark_delta,
                device_bounce_rate=device_bounce_rate,
                device_benchmark_bounce_rate=device_benchmark_bounce_rate,
                device_impressions=device_impressions,
                device_clicks=device_clicks,
                device_ctr=device_ctr,
                device_average_position=device_average_position,
                device_2_sessions=device_2_sessions,
                device_2_bounce_rate=device_2_bounce_rate,
                mobile_device_info=mobile_device_info,
                mobile_users=mobile_users,
                mobile_new_users=mobile_new_users,
                campaign_campaign_id=campaign_campaign_id,
                campaign_clicks=campaign_clicks,
                campaign_cost=campaign_cost,
                campaign_cpc=campaign_cpc,
                display_keywords=display_keywords,
                display_campaign=display_campaign,
                display_google_ads_ad_group=display_google_ads_ad_group,
                display_clicks=display_clicks,
                display_cost=display_cost,
                display_cpc=display_cpc,
                final_url=final_url,
                final_clicks=final_clicks,
                final_cost=final_cost,
                final_cpc=final_cpc,
                keyword=keyword,
                keyword_clicks=keyword_clicks,
                keyword_cost=keyword_cost,
                keyword_cpc=keyword_cpc,
                affinity_category_reach=affinity_category_reach,
                affinity_users=affinity_users,
                landing_page=landing_page,
                landing_impressions=landing_impressions,
                landing_clicks=landing_clicks,
                landing_ctr=landing_ctr,
                country=country,
                country_users=country_users,
                country_new_users=country_new_users,
                page_views=page_views,
                unique_page_views=unique_page_views,
                search_query=search_query,
                search_query_clicks=search_query_clicks,
                search_query_impressions=search_query_impressions,
                search_query_ctr=search_query_ctr,
                search_query_avg_position=search_query_avg_position,
                source=source,
                source_users=source_users,
                # source_new_users=source_new_users
            )
            

        messages.success(request, 'Data uploaded successfully')
        return redirect('analytics_data')
    
    else:
        ad_data = Analytics.objects.all()
        return render(request, 'Analytics.html', {'ad_data': ad_data})

def ad_data_list(request):
    ad_data = Analytics.objects.all()
    return render(request, 'Analytics.html', {'ad_data': ad_data})

def delete_rows(request):
    if request.method == 'POST':
        selected_ids = request.GET.get('ids').split(',')
        Analytics.objects.filter(id__in=selected_ids).delete()
    
    return redirect('analytics_data')

# def analytics_data(request):
#     data = Analytics.objects.all()
#     paginator = Paginator(data, 10)  # Show 10 items per page

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'ad_data': page_obj,
#     }

#     return render(request, 'Analytics.html', context)


# class ShowView(View):
#     def get(self, request):
#         show_value = request.GET.get('show', 'all')
        
#         # Add your logic here to handle different values of 'show'
#         if show_value == 'all':
#             # Retrieve all items from the database
#             data = Analytics.objects.all()
#         elif show_value == '10':
#             # Retrieve only 10 items from the database
#             data = Analytics.objects.all()[:10]
#         elif show_value == '20':
#             # Retrieve only 20 items from the database
#             data = Analytics.objects.all()[:20]
#         # Add more conditions for other possible values of 'show'
#         else:
#             # Default logic for handling unknown or invalid values of 'show'
#             data = []
        
#         context = {
#             'data': data,
#             'show_value': show_value,
#         }
#         return render(request, 'Analytics.html', context)
    
    
def Dash_Analytics(request):
    data = Analytics.objects.all()
    context = {
        "data" : data,
    }
    return render(request, "Analytics_Dashboard.html", context)