# Generated by Django 5.1 on 2024-11-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_desc',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_dir1',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_mail',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_rat',
            field=models.CharField(default=5, max_length=50),
        ),
    ]
