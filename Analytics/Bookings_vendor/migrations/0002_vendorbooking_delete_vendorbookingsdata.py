# Generated by Django 4.1.7 on 2023-06-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Bookings_vendor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VendorBooking",
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
                (
                    "vendor_name",
                    models.CharField(
                        choices=[
                            ("Vendor1", "Vendor 1"),
                            ("Vendor2", "Vendor 2"),
                            ("Vendor3", "Vendor 3"),
                        ],
                        max_length=100,
                    ),
                ),
                ("booking_date", models.DateField()),
                (
                    "service_gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                ("service_customer_name", models.CharField(max_length=100)),
                ("promotional_code", models.CharField(max_length=100)),
                ("promotional_code_count", models.IntegerField()),
                (
                    "promotional_code_amount",
                    models.DecimalField(decimal_places=2, max_digits=8),
                ),
                ("cancel_booking", models.BooleanField(default=False)),
                ("complete_booking", models.BooleanField(default=False)),
                ("pending_booking", models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name="VendorBookingsData",
        ),
    ]
