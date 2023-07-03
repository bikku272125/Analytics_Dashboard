# Generated by Django 4.1.7 on 2023-06-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gadwords", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyStats",
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
                ("date", models.DateField()),
                ("clicks", models.PositiveIntegerField()),
                ("cost", models.FloatField()),
                ("conversions", models.PositiveIntegerField()),
                ("cost_per_conversion", models.FloatField()),
                ("search_word", models.CharField(max_length=255)),
                ("search_word_clicks", models.PositiveIntegerField()),
                ("search_word_impressions", models.PositiveIntegerField()),
                ("search_word_cost", models.FloatField()),
                ("search_salon", models.CharField(max_length=255)),
                ("search_salon_clicks", models.PositiveIntegerField()),
                ("search_salon_impressions", models.PositiveIntegerField()),
                ("search_salon_cost", models.FloatField()),
                ("search_keyword", models.CharField(max_length=255)),
                ("search_keyword_clicks", models.PositiveIntegerField()),
                ("search_keyword_ctr", models.FloatField()),
                ("campaign_name", models.CharField(max_length=255)),
                ("optimization_score", models.FloatField()),
                ("network_name", models.CharField(max_length=255)),
                ("network_clicks", models.PositiveIntegerField()),
                ("network_cost", models.FloatField()),
                ("device_name", models.CharField(max_length=255)),
                ("device_cost", models.FloatField()),
                ("device_clicks", models.PositiveIntegerField()),
                ("device_conversion", models.PositiveIntegerField()),
                ("gender", models.CharField(max_length=255)),
                ("age_range", models.CharField(max_length=255)),
                ("gender_impression", models.PositiveIntegerField()),
                ("per_hour", models.CharField(max_length=255)),
                ("per_hour_impression", models.PositiveIntegerField()),
                ("per_day", models.CharField(max_length=255)),
                ("per_day_per_hour", models.CharField(max_length=255)),
                ("per_day_per_hour_impression", models.PositiveIntegerField()),
                ("campaigns_cost", models.FloatField()),
                ("campaigns_conversion", models.PositiveIntegerField()),
                ("campaigns_cost_per_conversion", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Daily Stats",
            },
        ),
        migrations.DeleteModel(
            name="AdData",
        ),
    ]