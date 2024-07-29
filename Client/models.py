from django.db import models

from adminPanel.models import City

# Create your models here.


class Client(models.Model):
    COMMERCIAL = 'Commercial'
    INDUSTRIAL = 'Industrial'
    CLIENT_TYPE_CHOICES = [
        (COMMERCIAL, 'Commercial'),
        (INDUSTRIAL, 'Industrial'),
    ]
    client_name = models.CharField(max_length=255, unique=True)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE_CHOICES)
    gst = models.CharField(max_length=255)
    ntn = models.CharField(max_length=255)
    director_name = models.CharField(max_length=255, null=True, blank=True)
    nic = models.CharField(max_length=255, null=True, blank=True)
    soap_manufacturer = models.BooleanField(default=False)
    director_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.client_name