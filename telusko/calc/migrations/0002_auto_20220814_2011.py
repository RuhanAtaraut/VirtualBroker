# Generated by Django 3.2.8 on 2022-08-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmess',
            name='price',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='addrooms',
            name='price',
            field=models.IntegerField(max_length=30),
        ),
    ]
