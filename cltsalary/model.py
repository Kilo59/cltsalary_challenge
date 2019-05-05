import peewee as pw

import mongoengine as me

sql_db = pw.SqliteDatabase("cities.sqlite3")
me.connect("cities")


class SQLEmployee(pw.Model):
    from peewee import AutoField, CharField, IntegerField

    employee_id = pw.AutoField()

    name = pw.CharField()
    # Some of these aren't defined, so let's not make them foreign keys.
    unit = pw.CharField(null=True)
    dept = pw.CharField(null=True)
    job_title = pw.CharField(null=True)

    salary = pw.IntegerField(null=True)
    hourly = pw.IntegerField(null=True)
    full_or_part = pw.CharField(max_length=1)
    reg_or_temp = pw.CharField(max_length=1)

    FID = pw.IntegerField()

    class Meta:
        database = sql_db


class MongoEmployee(me.Document):
    employee_id = me.SequenceField(collection_name="EmployeeTotal")

    name = me.StringField(required=True)
    unit = me.StringField(required=False)
    dept = me.StringField(required=False)
    job_title = me.StringField(required=False)

    salary = me.IntField(required=False)
    hourly = me.IntField(required=False)
    full_or_part = me.StringField(max_length=1, required=True)
    reg_or_temp = me.StringField(max_length=1, required=True)

    FID = me.IntField()
