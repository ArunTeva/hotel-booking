# Generated by Django 4.1.1 on 2022-10-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_booking_app', '0015_alter_booking_check_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_info',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
