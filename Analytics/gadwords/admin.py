from django.contrib import admin
from .models import DailyStats

class DailyStatsAdmin(admin.ModelAdmin):
    list_display = ('date', 'clicks', 'cost', 'conversions', 'cost_per_conversion', 'search_word',
                    'search_word_clicks', 'search_word_impressions', 'search_word_cost', 'search_salon',
                    'search_salon_clicks', 'search_salon_impressions', 'search_salon_cost', 'search_keyword',
                    'search_keyword_clicks', 'search_keyword_ctr', 'campaign_name', 'optimization_score',
                    'network_name', 'network_clicks', 'network_cost', 'device_name', 'device_cost',
                    'device_clicks', 'device_conversion', 'gender', 'age_range', 'gender_impression',
                    'per_hour', 'per_hour_impression', 'per_day', 'per_day_per_hour',
                    'per_day_per_hour_impression', 'campaigns_cost', 'campaigns_conversion',
                    'campaigns_cost_per_conversion')
    list_filter = ('date', 'campaign_name')
    search_fields = ('campaign_name',)

admin.site.register(DailyStats, DailyStatsAdmin)
