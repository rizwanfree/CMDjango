from django.db import models

# Create your models here.

class City(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name