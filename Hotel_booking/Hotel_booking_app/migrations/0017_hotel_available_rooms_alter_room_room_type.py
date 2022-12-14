# Generated by Django 4.1.1 on 2022-10-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_booking_app', '0016_alter_room_room_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='available_rooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('SINGLE', 'SINGLE'), ('DOUBLE', 'DOUBLE')], default='SINGLE', max_length=20),
        ),
    ]
