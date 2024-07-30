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
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.short_name
    
class Terminal(models.Model):
    id = models.AutoField(primary_key=True)
    terminal_name = models.CharField(max_length=250, unique=True)
    short_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_name
    
class ShippingLine(models.Model):
    id = models.AutoField(primary_key=True)
    line_name = models.CharField(max_length=250, unique=True)
    short_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.short_name
    

class IGM(models.Model):
    id = models.AutoField(primary_key=True)
    igm_number = models.IntegerField()
    igm_date = models.DateField()
    vessel = models.CharField(max_length=200)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.igm_number}/{self.igm_date.year}"
    

class Item(models.Model):
    DUTY_TYPE_CHOICE = (
        ('%', '%'),
        ('F', 'F'),
    )
    item_name = models.CharField(max_length=255)
    hs_code = models.CharField(max_length=50, blank=True, null=True)
    custom_duty_type = models.CharField(max_length=5, choices=DUTY_TYPE_CHOICE, blank=True, null=True)
    custom_duty_rate = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    additional_custom_duty_type = models.CharField(max_length=5, choices=DUTY_TYPE_CHOICE, blank=True, null=True)
    additional_custom_duty_rate = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    regulatory_duty_type = models.CharField(max_length=5, choices=DUTY_TYPE_CHOICE, blank=True, null=True)
    regulatory_duty_rate = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    sales_tax_rate = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    additional_sales_tax_rate = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    income_tax_rate = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    psqc_rate = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    wharfage_rate = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)

    def __str__(self):
        return self.item_name