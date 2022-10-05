from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *
# Register your models here.
myuser=get_user_model()

admin.site.register(myuser)

@admin.register(Hotel)

class Hotel(admin.ModelAdmin):
    list_display=['name','city',]

@admin.register(Room)
class Room(admin.ModelAdmin):
    list_display=['hotel','room_no','room_price']
admin.site.register(Booking)
