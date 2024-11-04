# Generated by Django 3.2.8 on 2022-08-14 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Copy_User',
            fields=[
                ('copy_user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('copy_firstname', models.CharField(max_length=30)),
                ('copy_lastname', models.CharField(max_length=30)),
                ('copy_uemail', models.CharField(max_length=30)),
                ('copy_contactnumber', models.CharField(max_length=30)),
                ('copy_city', models.CharField(max_length=30)),
                ('copy_address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mess_cities',
            fields=[
                ('mess_cities_id', models.AutoField(primary_key=True, serialize=False)),
                ('mess_city_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mess_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=10)),
                ('mess_price', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Otp_user',
            fields=[
                ('otp_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('otp_firstname', models.CharField(max_length=30)),
                ('otp_lastname', models.CharField(max_length=30)),
                ('otp_uemail', models.CharField(max_length=30)),
                ('otp_contactnumber', models.CharField(max_length=30)),
                ('otp_city', models.CharField(max_length=30)),
                ('otp_address', models.CharField(max_length=30)),
                ('otp_password', models.CharField(max_length=30)),
                ('otp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phonenumber', models.IntegerField()),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room_cities',
            fields=[
                ('room_cities_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_city_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room_Areas',
            fields=[
                ('room_area_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_area_name', models.CharField(max_length=30, unique=True)),
                ('rc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Room_Areas', to='calc.room_cities')),
            ],
        ),
        migrations.CreateModel(
            name='Mess_Areas',
            fields=[
                ('mess_area_id', models.AutoField(primary_key=True, serialize=False)),
                ('mess_area_name', models.CharField(max_length=30, unique=True)),
                ('mc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.mess_cities')),
            ],
        ),
        migrations.CreateModel(
            name='AddRooms',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=30)),
                ('rtype', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('c_u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AddRooms', to='calc.copy_user')),
                ('ra_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AddRooms', to='calc.room_areas')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AddRooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddMess',
            fields=[
                ('mess_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('messtype', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=30)),
                ('c_u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AddMess', to='calc.copy_user')),
                ('ma_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.mess_areas')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]