# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departments(models.Model):
    id_department = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'departments'


class Education(models.Model):
    id_education = models.IntegerField(primary_key=True)
    id_employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='id_employee')
    type_education = models.CharField(max_length=255)
    name_education = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'education'


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    pol = models.IntegerField()
    date = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    id_position = models.ForeignKey('Timetable', on_delete=models.CASCADE, db_column='id_position')

    class Meta:
        managed = False
        db_table = 'employee'


class Pasports(models.Model):
    id_pasport = models.IntegerField(primary_key=True)
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='id_employee')
    number = models.CharField(max_length=255)
    name_give = models.CharField(max_length=255)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'pasports'


class Timetable(models.Model):
    id_position = models.IntegerField(primary_key=True)
    id_department = models.ForeignKey(Departments, on_delete=models.CASCADE, db_column='id_department')
    name = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'timetable'
