from django.db import models

class VendorBooking(models.Model):
    VENDOR_CHOICES = [
        ('Vendor1', 'Vendor 1'),
        ('Vendor2', 'Vendor 2'),
        ('Vendor3', 'Vendor 3'),
        # Add more vendor choices as needed
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        # Add more gender choices as needed
    ]
    
    vendor_name = models.CharField(max_length=100, choices=VENDOR_CHOICES)
    booking_date = models.DateField()
    service_gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    service_customer_name = models.CharField(max_length=100)
    promotional_code = models.CharField(max_length=100)
    promotional_code_count = models.IntegerField()
    promotional_code_amount = models.DecimalField(max_digits=8, decimal_places=2)
    cancel_booking = models.BooleanField(default=False)
    complete_booking = models.BooleanField(default=False)
    pending_booking = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.vendor_name} - {self.service_customer_name}'
