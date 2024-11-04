from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room_Detail(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    price = models.IntegerField()
    

class Mess_Detail(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    mess_price = models.CharField(max_length=15)

class Register(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    phonenumber=models.IntegerField()
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)

# Copy_user --------------------
class Copy_User(models.Model):
    copy_user_id = models.IntegerField(primary_key=True)
    copy_firstname = models.CharField(max_length=30)
    copy_lastname = models.CharField(max_length=30)
    copy_uemail = models.CharField(max_length=30)
    copy_contactnumber = models.CharField(max_length=30)
    copy_city = models.CharField(max_length=30)
    copy_address = models.CharField(max_length=30)

# Rooms tables -------------------------

class Room_cities(models.Model):
    room_cities_id = models.AutoField(primary_key=True)
    room_city_name = models.CharField(max_length=30, unique=True)


class Room_Areas(models.Model):
    room_area_id = models.AutoField(primary_key=True)
    rc_id = models.ForeignKey(Room_cities, on_delete=models.CASCADE, related_name='Room_Areas')
    room_area_name = models.CharField(max_length=30, unique=True)


class AddRooms(models.Model):                       # AddRooms == RoomDetails
    room_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='AddRooms')
    c_u_id = models.ForeignKey(Copy_User, on_delete=models.CASCADE, related_name='AddRooms')
    ra_id = models.ForeignKey(Room_Areas, on_delete=models.CASCADE, related_name='AddRooms')
    category = models.CharField(max_length=30)
    rtype = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    price = models.IntegerField(max_length=30)


# Mess tables -----------------------------------

class Mess_cities(models.Model):
    mess_cities_id = models.AutoField(primary_key=True)
    mess_city_name = models.CharField(max_length=30, unique=True)



class Mess_Areas(models.Model):
    mess_area_id = models.AutoField(primary_key=True)
    mc_id = models.ForeignKey(Mess_cities, on_delete=models.CASCADE)
    mess_area_name = models.CharField(max_length=30, unique=True)


class AddMess(models.Model):                            # MessRooms == MessDetails
    mess_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    c_u_id = models.ForeignKey(Copy_User, on_delete=models.CASCADE, related_name='AddMess')
    ma_id = models.ForeignKey(Mess_Areas, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    messtype = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    price = models.IntegerField(max_length=30)


class Otp_user(models.Model):
    otp_user_id = models.AutoField(primary_key=True)
    otp_firstname = models.CharField(max_length=30)
    otp_lastname = models.CharField(max_length=30)
    otp_uemail = models.CharField(max_length=30)
    otp_contactnumber = models.CharField(max_length=30)
    otp_city =models.CharField(max_length=30)
    otp_address = models.CharField(max_length=30)
    otp_password = models.CharField(max_length=30)
    otp = models.CharField(max_length=30)










