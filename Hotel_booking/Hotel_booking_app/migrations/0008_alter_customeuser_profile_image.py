# Generated by Django 4.1.1 on 2022-10-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel_booking_app', '0007_alter_customeuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='profile_image',
            field=models.FileField(upload_to='myProfiles/'),
        ),
    ]