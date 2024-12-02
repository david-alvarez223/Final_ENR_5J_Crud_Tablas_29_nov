# Generated by Django 5.1.3 on 2024-11-29 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=50)),
                ('client_rating', models.IntegerField()),
            ],
        ),
    ]