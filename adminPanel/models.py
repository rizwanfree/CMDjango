from django.db import models

# Create your models here.

class City(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name
    

class Port(models.Model):
    id = models.AutoField(primary_key=True)
    port_name = models.CharField(max_length=250, unique=True)
    short_name = models.CharField(max_length=50)

    def __str__(self):
        return self.short_name
    

class IGM(models.Model):
    id = models.AutoField(primary_key=True)
    igm_number = models.IntegerField()
    igm_date = models.DateField()
    vessel = models.CharField(max_length=200)
    port_id = models.ForeignKey(Port, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.igm_number}/{self.igm_date.year}"