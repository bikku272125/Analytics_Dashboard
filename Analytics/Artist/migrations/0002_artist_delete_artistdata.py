# Generated by Django 4.1.7 on 2023-06-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Artist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Artist",
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
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("is_active", models.BooleanField(default=True)),
                ("is_inactive", models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name="ArtistData",
        ),
    ]