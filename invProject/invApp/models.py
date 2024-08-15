from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    delivered_date = models.DateTimeField(default=datetime.now())
    product_image = models.ImageField(upload_to="invApp/products/", default="defaults/default.png")
    
    def __str__(self):
        return self.product_name