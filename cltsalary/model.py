import peewee

# from mongoengine import *
sql_db = peewee.SqliteDatabase("cities.sqlite3")


class Employee(peewee.Model):
    from peewee import AutoField, CharField, IntegerField

    employee_id = AutoField()

    name = CharField()
    # Some of these aren't defined, so let's not make them foreign keys.
    unit = CharField(null=True)
    dept = CharField(null=True)
    job_title = CharField(null=True)

    salary = IntegerField(null=True)
    hourly = IntegerField(null=True)
    full_or_part = CharField(max_length=1)
    reg_or_temp = CharField(max_length=1)

    FID = IntegerField()

    class Meta:
        database = sql_db
