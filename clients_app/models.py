from django.db import models

# Create your models here.
class Client(models.Model):
    client_id=models.CharField(primary_key=True,max_length=10)
    client_name=models.CharField(max_length=50)
    client_freq=models.CharField(max_length=50, default="null")
    client_rating=models.IntegerField()

    def __str__(self):
        return self.client_name