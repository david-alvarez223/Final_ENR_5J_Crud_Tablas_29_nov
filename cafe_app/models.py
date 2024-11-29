from django.db import models

# Create your models here.
class Cafe(models.Model):
    cafe_id=models.CharField(primary_key=True,max_length=10)
    cafe_dir=models.CharField(max_length=50)
    cafe_man=models.CharField(max_length=50)
    cafe_phone=models.CharField(max_length=50)
    cafe_city=models.CharField(max_length=50)
    cafe_mail=models.CharField(max_length=50)
    cafe_num=models.IntegerField()

    def __str__(self):
        return self.cafe_id