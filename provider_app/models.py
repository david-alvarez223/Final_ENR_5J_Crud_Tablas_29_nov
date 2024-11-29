from django.db import models

# Create your models here.
class Provider(models.Model):
    provider_id=models.CharField(primary_key=True,max_length=10)
    provider_name=models.CharField(max_length=50)
    provider_dir=models.CharField(max_length=50)

    def __str__(self):
        return self.provider_name