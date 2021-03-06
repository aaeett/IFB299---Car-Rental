# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('username', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.IntegerField(blank=True, db_column='Car_id', null=True)),
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
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(db_column='Customer_ID')),
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
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
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
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField(blank=True, db_column='Order_id', null=True, unique=True)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField(blank=True, db_column='Store_id', null=True)),
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
    ]
