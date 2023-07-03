from django.db import models

class ArtistBooking(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    STATUS_CHOICES = (
        ('Complete', 'Complete'),
        ('Cancel', 'Cancel'),
        ('Pending', 'Pending'),
    )

    per_day = models.IntegerField()
    time = models.TimeField()
    customer_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    artist_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    discount_used = models.BooleanField(default=False)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.customer_name}'s booking on {self.per_day}"
