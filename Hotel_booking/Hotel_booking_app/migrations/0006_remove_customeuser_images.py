# Generated by Django 4.1.1 on 2022-10-03 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_booking_app', '0005_alter_customeuser_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeuser',
            name='images',
        ),
    ]
