from django.contrib import admin
from calc.models import Room_Detail,Mess_Detail,Register
from .models import AddRooms, AddMess, Room_Areas, Room_cities, Mess_Areas, Mess_cities, Otp_user, Copy_User
# Register your models here.

@admin.register(Room_Detail)
class Room_DetailAdmin(admin.ModelAdmin):
    list_display = ('name','city', 'address', 'contact','price')
    ordering = ('name',)
    search_fields = ('name', 'city')

admin.site.register(Mess_Detail)
class Mess_DetailAdmin(admin.ModelAdmin):
    list_display=('name','city','address','contact','mess_price')
    ordering = ('name',)
    search_fields=('name','city')

admin.site.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display=('first_name','Last_name','email','phonenumber','password','cpassword')
    ordering = ('name',)
    search_fields=('name','email')






@admin.register(AddRooms)
class AddRoomsAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'u_id', 'c_u_id', 'category', 'rtype', 'address', 'ra_id', 'price',)


@admin.register(AddMess)
class AddMessAdmin(admin.ModelAdmin):
    list_display = ('mess_id', 'u_id', 'c_u_id', 'name', 'messtype', 'address', 'price')


@admin.register(Room_Areas)
class Room_AreasAdmin(admin.ModelAdmin):
    list_display = ('room_area_id', 'rc_id', 'room_area_name',)

@admin.register(Room_cities)
class Room_citiesAdmin(admin.ModelAdmin):
    list_display = ('room_cities_id', 'room_city_name',)

@admin.register(Mess_cities)
class Mess_citiesAdmin(admin.ModelAdmin):
    list_display = ('mess_cities_id', 'mess_city_name',)


@admin.register(Mess_Areas)
class Mess_AreasAdmin(admin.ModelAdmin):
    list_display = ('mess_area_id', 'mess_area_name',)

@admin.register(Otp_user)
class Otp_userAdmin(admin.ModelAdmin):
    list_display = ('otp_user_id', 'otp_uemail',)

@admin.register(Copy_User)
class Copy_UserAdmin(admin.ModelAdmin):
    list_display = ('copy_user_id', 'copy_firstname', 'copy_lastname', 'copy_uemail', 'copy_contactnumber', 'copy_city',
                    'copy_address')
