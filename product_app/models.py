from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.CharField(primary_key=True,max_length=10)
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    product_type=models.CharField(max_length=50, default="unknown")

    def __str__(self):
        return self.product_name