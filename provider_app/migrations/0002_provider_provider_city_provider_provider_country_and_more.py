# Generated by Django 5.1 on 2024-11-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='provider_city',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='provider',
            name='provider_country',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='provider',
            name='provider_mail',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='provider',
            name='provider_phone',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]