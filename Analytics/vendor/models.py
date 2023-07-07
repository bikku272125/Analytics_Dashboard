from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_active = models.BooleanField(default=True)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return self.name
