# Generated by Django 4.1.7 on 2023-06-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ganalytics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Analytics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("default_channel_grouping", models.CharField(max_length=255)),
                ("default_sessions", models.IntegerField()),
                ("default_new_users", models.IntegerField()),
                ("browser", models.CharField(max_length=255)),
                ("browser_users", models.IntegerField()),
                ("browser_new_users", models.IntegerField()),
                ("browser_sessions", models.IntegerField()),
                ("browser_bounce_rate", models.FloatField()),
                ("browser_pages_session", models.FloatField()),
                ("day_index", models.DateField()),
                ("day_users", models.IntegerField()),
                ("day_sessions", models.IntegerField()),
                ("day_benchmark_sessions", models.IntegerField()),
                ("device_category", models.CharField(max_length=255)),
                ("device_sessions_benchmark_delta", models.IntegerField()),
                ("device_sessions", models.IntegerField()),
                ("device_benchmark_sessions", models.IntegerField()),
                ("device_new_sessions_benchmark_delta", models.IntegerField()),
                ("device_new_sessions", models.IntegerField()),
                ("device_benchmark_new_sessions", models.IntegerField()),
                ("device_new_users_benchmark_delta", models.IntegerField()),
                ("device_new_users", models.IntegerField()),
                ("device_benchmark_new_users", models.IntegerField()),
                ("device_pages_session_benchmark_delta", models.FloatField()),
                ("device_pages_session", models.FloatField()),
                ("device_benchmark_pages_session", models.FloatField()),
                ("device_avg_session_duration", models.FloatField()),
                ("device_avg_benchmark_session_duration", models.FloatField()),
                ("device_bounce_rate_benchmark_delta", models.FloatField()),
                ("device_bounce_rate", models.FloatField()),
                ("device_benchmark_bounce_rate", models.FloatField()),
                ("device_impressions", models.IntegerField()),
                ("device_clicks", models.IntegerField()),
                ("device_ctr", models.FloatField()),
                ("device_average_position", models.FloatField()),
                ("device_2_sessions", models.IntegerField()),
                ("device_2_bounce_rate", models.FloatField()),
                ("mobile_device_info", models.CharField(max_length=255)),
                ("mobile_users", models.IntegerField()),
                ("mobile_new_users", models.IntegerField()),
                ("campaign_campaign_id", models.CharField(max_length=255)),
                ("campaign_clicks", models.IntegerField()),
                ("campaign_cost", models.FloatField()),
                ("campaign_cpc", models.FloatField()),
                ("display_keywords", models.CharField(max_length=255)),
                ("display_campaign", models.CharField(max_length=255)),
                ("display_google_ads_ad_group", models.CharField(max_length=255)),
                ("display_clicks", models.IntegerField()),
                ("display_cost", models.FloatField()),
                ("display_cpc", models.FloatField()),
                ("final_url", models.CharField(max_length=255)),
                ("final_clicks", models.IntegerField()),
                ("final_cost", models.FloatField()),
                ("final_cpc", models.FloatField()),
                ("keyword", models.CharField(max_length=255)),
                ("keyword_clicks", models.IntegerField()),
                ("keyword_cost", models.FloatField()),
                ("keyword_cpc", models.FloatField()),
                ("video_campaign_id", models.CharField(max_length=255)),
                ("video_paid_views", models.IntegerField()),
                ("video_cost", models.FloatField()),
                ("video_cpv", models.FloatField()),
                ("affinity_category_reach", models.CharField(max_length=255)),
                ("affinity_users", models.IntegerField()),
                ("landing_page", models.CharField(max_length=255)),
                ("landing_impressions", models.IntegerField()),
                ("landing_clicks", models.IntegerField()),
                ("landing_ctr", models.FloatField()),
                ("country", models.CharField(max_length=255)),
                ("country_users", models.IntegerField()),
                ("country_new_users", models.IntegerField()),
                ("page_views", models.IntegerField()),
                ("unique_page_views", models.IntegerField()),
                ("search_query", models.CharField(max_length=255)),
                ("search_query_clicks", models.IntegerField()),
                ("search_query_impressions", models.IntegerField()),
                ("search_query_ctr", models.FloatField()),
                ("search_query_avg_position", models.FloatField()),
                ("source", models.CharField(max_length=255)),
                ("source_users", models.IntegerField()),
                ("source_new_users", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="AnalyticsData",
        ),
    ]
