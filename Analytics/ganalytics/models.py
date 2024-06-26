from django.db import models

class Analytics(models.Model):
    default_channel_grouping = models.CharField(max_length=255)
    default_sessions = models.CharField(max_length=255)
    default_new_users = models.CharField(max_length=255)
    browser = models.CharField(max_length=255)
    browser_users = models.CharField(max_length=255)
    browser_new_users = models.CharField(max_length=255)
    browser_sessions = models.CharField(max_length=255)
    browser_bounce_rate = models.CharField(max_length=255)
    browser_pages_session = models.CharField(max_length=255)
    day_index = models.CharField(max_length=255)
    day_users = models.CharField(max_length=255)
    day_sessions = models.CharField(max_length=255)
    day_benchmark_sessions = models.CharField(max_length=255)
    device_category = models.CharField(max_length=255)
    device_sessions_benchmark_delta = models.CharField(max_length=255)
    device_sessions = models.CharField(max_length=255)
    device_benchmark_sessions = models.CharField(max_length=255)
    device_new_sessions_benchmark_delta = models.CharField(max_length=255)
    device_new_sessions = models.CharField(max_length=255)
    device_benchmark_new_sessions = models.CharField(max_length=255)
    device_new_users_benchmark_delta = models.CharField(max_length=255)
    device_benchmark_new_users = models.CharField(max_length=255)
    device_pages_session_benchmark_delta = models.CharField(max_length=255)
    device_pages_session = models.CharField(max_length=255)
    device_benchmark_pages_session = models.CharField(max_length=255)
    device_avg_session_duration = models.CharField(max_length=255)
    device_avg_benchmark_session_duration = models.CharField(max_length=255)
    device_bounce_rate_benchmark_delta = models.CharField(max_length=255)
    device_bounce_rate = models.CharField(max_length=255)
    device_benchmark_bounce_rate = models.CharField(max_length=255)
    device_impressions = models.CharField(max_length=255)
    device_clicks = models.CharField(max_length=255)
    device_ctr = models.CharField(max_length=255)
    device_average_position = models.CharField(max_length=255)
    device_2_sessions = models.CharField(max_length=255)
    device_2_bounce_rate = models.CharField(max_length=255)
    mobile_device_info = models.CharField(max_length=255)
    mobile_users = models.CharField(max_length=255)
    mobile_new_users = models.CharField(max_length=255)
    campaign_campaign_id = models.CharField(max_length=255)
    campaign_clicks = models.CharField(max_length=255)
    campaign_cost = models.CharField(max_length=255)
    campaign_cpc = models.CharField(max_length=255)
    display_keywords = models.CharField(max_length=255)
    display_campaign = models.CharField(max_length=255)
    display_google_ads_ad_group = models.CharField(max_length=255)
    display_clicks = models.CharField(max_length=255)
    display_cost = models.CharField(max_length=255)
    display_cpc = models.CharField(max_length=255)
    final_url = models.CharField(max_length=255)
    final_clicks = models.CharField(max_length=255)
    final_cost = models.CharField(max_length=255)
    final_cpc = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    keyword_clicks = models.CharField(max_length=255)
    keyword_cost = models.CharField(max_length=255)
    keyword_cpc = models.CharField(max_length=255)
    affinity_category_reach = models.CharField(max_length=255)
    affinity_users = models.CharField(max_length=255)
    landing_page = models.CharField(max_length=255)
    landing_impressions = models.CharField(max_length=255)
    landing_clicks = models.CharField(max_length=255)
    landing_ctr = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    country_users = models.CharField(max_length=255)
    country_new_users = models.CharField(max_length=255)
    page_views = models.CharField(max_length=255)
    unique_page_views = models.CharField(max_length=255)
    search_query = models.CharField(max_length=255)
    search_query_clicks = models.CharField(max_length=255)
    search_query_impressions = models.CharField(max_length=255)
    search_query_ctr = models.CharField(max_length=255)
    search_query_avg_position = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    source_users = models.CharField(max_length=255)
    source_new_users = models.CharField(max_length=255)

    def __str__(self):
        return self.default_channel_grouping
