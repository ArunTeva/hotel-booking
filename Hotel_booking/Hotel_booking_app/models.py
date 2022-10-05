from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from enum import auto, unique
from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import *
from django.utils import timezone
# Create your models here.

class CustomeUser(AbstractUser):
    username=None
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('OTHER','Other')
    )

    ROLL=(
        ('User','User'),
        ('Manager','Manager')
    )
    first_name=models.CharField(max_length=50,null=True,blank=True)
    last_name=models.CharField(max_length=50,null=True,blank=True)

    email=models.EmailField(unique=True)
    profile_image=models.ImageField(upload_to = "myProfiles",null=True,blank=True)
    mobile=models.CharField(max_length=12,null=True,blank=True)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=10,null=True,blank=True)
    dob=models.DateField(default=timezone.now,null=True,blank=True)
    roll=models.CharField(choices=ROLL,max_length=10,default='User')
    address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)



    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()

class Hotel(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=150,null=True,blank=True)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=12,null=True,blank=True)
    Hotel_image=models.ImageField(upload_to='hotel')
    available_rooms=models.IntegerField(default=1)
    rating=models.IntegerField(default=1)
    hotel_info=models.CharField(max_length=500,null=True,blank=True)

    def __str__(self) :
        return self.name

class Room(models.Model):
    Room_CHOICE=(
        ('SINGLE','SINGLE'),
        ('DOUBLE','DOUBLE'),
    )
    room_no=models.IntegerField(default=100)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room_type=models.CharField(choices=Room_CHOICE,max_length=20,default='SINGLE')
    room_image=models.ImageField(upload_to='rooms')
    room_price=models.FloatField()
    room_availability=models.BooleanField()
    room_info=models.CharField(max_length=500,null=True,blank=True)

    def __str__(self) :
        return self.room_type

class Booking(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    select_room=models.ManyToManyField(Room)
    check_in=models.DateField()
    check_out=models.DateField()
    Adult=models.IntegerField(default=1)
    children=models.IntegerField(default=0)

   