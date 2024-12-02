from django.db import models

# Create your models here.
class Inventory(models.Model):
    inventory_id=models.CharField(primary_key=True,max_length=10)
    inventory_name=models.CharField(max_length=50)
    inventory_quantity=models.IntegerField()
    inventory_capacity=models.IntegerField()
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.inventory_name