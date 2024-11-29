from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id=models.CharField(primary_key=True,max_length=10)
    employee_name=models.CharField(max_length=50)
    employee_mail=models.CharField(max_length=50, default="unknown")
    employee_dir1=models.CharField(max_length=50, default="unknown")
    employee_dir=models.CharField(max_length=50)
    employee_desc=models.CharField(max_length=50, default="null")
    employee_rat=models.CharField(max_length=50, default=5)

    def __str__(self):
        return self.employee_name