# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Car(models.Model):
    car_id = models.IntegerField(db_column='Car_id', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    car_make_model = models.TextField(db_column='Car_Make_Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    car_model = models.TextField(db_column='Car_Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    car_series = models.TextField(db_column='Car_Series', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    car_seriesyear = models.IntegerField(db_column='Car_SeriesYear', blank=True, null=True)  # Field name made lowercase.
    car_pricenew = models.IntegerField(db_column='Car_PriceNew', blank=True, null=True)  # Field name made lowercase.
    car_enginesize = models.TextField(db_column='Car_EngineSize', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    car_fuelsystem = models.TextField(db_column='Car_FuelSystem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    car_tankcapacity = models.TextField(db_column='Car_TankCapacity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    car_power = models.TextField(db_column='Car_Power', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    car_seatingcapacity = models.IntegerField(db_column='Car_SeatingCapacity', blank=True, null=True)  # Field name made lowercase.
    car_bodytype = models.TextField(db_column='Car_BodyType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    car_drive = models.TextField(db_column='Car_Drive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    car_wheelbase = models.TextField(db_column='Car_Wheelbase', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Car'


class Customers(models.Model):
    customer_id = models.IntegerField(db_column='Customer_ID', null=False, primary_key=True)  # Field name made lowercase.
    customer_name = models.TextField(db_column='Customer_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    customer_phone = models.IntegerField(db_column='Customer_Phone', blank=True, null=True)  # Field name made lowercase.
    customer_address = models.TextField(db_column='Customer_Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    customer_birthday = models.DateField(db_column='Customer_birthday', blank=True, null=True)  # Field name made lowercase.
    customer_occupation = models.TextField(db_column='Customer_occupation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    customer_gender = models.TextField(db_column='Customer_Gender', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Customers'


class Orders(models.Model):
    order_id = models.TextField(db_column='Order_id', unique=True, blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.
    order_createdate = models.DateField(db_column='Order_CreateDate', blank=True, null=True)  # Field name made lowercase.
    prder_pickupdate = models.DateField(db_column='Prder_pickupDate', blank=True, null=True)  # Field name made lowercase.
    order_pickupstore = models.TextField(db_column='Order_pickupStore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickup_store_name = models.TextField(db_column='Pickup_store_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickup_store_address = models.TextField(db_column='Pickup_store_Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickup_store_phone = models.TextField(db_column='Pickup_Store_Phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickup_store_city = models.TextField(db_column='Pickup_Store_city', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickup_store_state_name = models.TextField(db_column='Pickup_Store_State_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    order_return_date = models.DateField(db_column='Order_Return_Date', blank=True, null=True)  # Field name made lowercase.
    order_returnstore = models.TextField(db_column='Order_ReturnStore', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    return_store_name = models.TextField(db_column='Return_Store_name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    return_store_address = models.TextField(db_column='Return_Store_Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    return_store_phone = models.TextField(db_column='Return_Store_Phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    return_store_city = models.TextField(db_column='Return_store_city', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    return_store_state = models.CharField(db_column='Return_store_State', max_length=3, blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customers, models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)  # Field name made lowercase.
    car = models.ForeignKey(Car, models.DO_NOTHING, db_column='Car_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'


class Store(models.Model):
    store_id = models.IntegerField(db_column='Store_id', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    store_name = models.TextField(db_column='Store_name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    store_address = models.TextField(db_column='Store_Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    store_phone = models.TextField(db_column='Store_phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    store_city = models.TextField(db_column='Store_City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    store_state_name = models.TextField(db_column='Store_State_name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Store'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
