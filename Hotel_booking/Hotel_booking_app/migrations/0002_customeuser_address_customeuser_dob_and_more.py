# Generated by Django 4.1.1 on 2022-09-30 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customeuser',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AddField(
            model_name='customeuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('OTHER', 'Other')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customeuser',
            name='roll',
            field=models.CharField(choices=[('User', 'User'), ('Manager', 'Manager')], default=2, max_length=10),
            preserve_default=False,
        ),
    ]