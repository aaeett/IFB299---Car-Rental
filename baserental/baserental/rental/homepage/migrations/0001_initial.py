# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-17 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.IntegerField(db_column='Customer_ID', primary_key=True, serialize=False)),
                ('customer_name', models.TextField(blank=True, db_column='Customer_Name', null=True)),
                ('customer_phone', models.IntegerField(blank=True, db_column='Customer_Phone', null=True)),
                ('customer_address', models.TextField(blank=True, db_column='Customer_Address', null=True)),
                ('customer_birthday', models.DateField(blank=True, db_column='Customer_birthday', null=True)),
                ('customer_occupation', models.TextField(blank=True, db_column='Customer_occupation', null=True)),
                ('customer_gender', models.TextField(blank=True, db_column='Customer_Gender', null=True)),
            ],
            options={
                'db_table': 'Customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.TextField(blank=True, db_column='Order_id', primary_key=True, serialize=False, unique=True)),
                ('order_createdate', models.DateField(blank=True, db_column='Order_CreateDate', null=True)),
                ('prder_pickupdate', models.DateField(blank=True, db_column='Prder_pickupDate', null=True)),
                ('order_pickupstore', models.TextField(blank=True, db_column='Order_pickupStore', null=True)),
                ('pickup_store_name', models.TextField(blank=True, db_column='Pickup_store_Name', null=True)),
                ('pickup_store_address', models.TextField(blank=True, db_column='Pickup_store_Address', null=True)),
                ('pickup_store_phone', models.TextField(blank=True, db_column='Pickup_Store_Phone', null=True)),
                ('pickup_store_city', models.TextField(blank=True, db_column='Pickup_Store_city', null=True)),
                ('pickup_store_state_name', models.TextField(blank=True, db_column='Pickup_Store_State_Name', null=True)),
                ('order_return_date', models.DateField(blank=True, db_column='Order_Return_Date', null=True)),
                ('order_returnstore', models.TextField(blank=True, db_column='Order_ReturnStore', null=True)),
                ('return_store_name', models.TextField(blank=True, db_column='Return_Store_name', null=True)),
                ('return_store_address', models.TextField(blank=True, db_column='Return_Store_Address', null=True)),
                ('return_store_phone', models.TextField(blank=True, db_column='Return_Store_Phone', null=True)),
                ('return_store_city', models.TextField(blank=True, db_column='Return_store_city', null=True)),
                ('return_store_state', models.CharField(blank=True, db_column='Return_store_State', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.IntegerField(blank=True, db_column='Store_id', primary_key=True, serialize=False)),
                ('store_name', models.TextField(blank=True, db_column='Store_name', null=True)),
                ('store_address', models.TextField(blank=True, db_column='Store_Address', null=True)),
                ('store_phone', models.TextField(blank=True, db_column='Store_phone', null=True)),
                ('store_city', models.TextField(blank=True, db_column='Store_City', null=True)),
                ('store_state_name', models.TextField(blank=True, db_column='Store_State_name', null=True)),
            ],
            options={
                'db_table': 'Store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.IntegerField(blank=True, db_column='Car_id', primary_key=True, serialize=False)),
                ('car_make_model', models.TextField(blank=True, db_column='Car_Make_Model', null=True)),
                ('car_model', models.TextField(blank=True, db_column='Car_Model', null=True)),
                ('car_series', models.TextField(blank=True, db_column='Car_Series', null=True)),
                ('car_seriesyear', models.IntegerField(blank=True, db_column='Car_SeriesYear', null=True)),
                ('car_pricenew', models.IntegerField(blank=True, db_column='Car_PriceNew', null=True)),
                ('car_enginesize', models.TextField(blank=True, db_column='Car_EngineSize', null=True)),
                ('car_fuelsystem', models.TextField(blank=True, db_column='Car_FuelSystem', null=True)),
                ('car_tankcapacity', models.TextField(blank=True, db_column='Car_TankCapacity', null=True)),
                ('car_power', models.TextField(blank=True, db_column='Car_Power', null=True)),
                ('car_seatingcapacity', models.IntegerField(blank=True, db_column='Car_SeatingCapacity', null=True)),
                ('car_bodytype', models.TextField(blank=True, db_column='Car_BodyType', null=True)),
                ('car_drive', models.TextField(blank=True, db_column='Car_Drive', null=True)),
                ('car_wheelbase', models.TextField(blank=True, db_column='Car_Wheelbase', null=True)),
            ],
            options={
                'db_table': 'Car',
            },
        ),
    ]