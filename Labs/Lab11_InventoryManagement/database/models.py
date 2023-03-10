from .db import db

class Vehicle(db.Document):
    reg = db.StringField(required = True)
    model = db.StringField(required=True)

class Contacts(db.Document):
    name = db.StringField(required=True)
    mobile = db.StringField(required=True)
    phone = db.StringField()
    city = db.StringField()
    web = db.StringField()
    insta = db.StringField()
    fb = db.StringField()
    email = db.StringField()

class Student(db.Document):
    rollno = db.StringField(required=True)
    name = db.StringField(required=True)
    cgpa = db.FloatField()

class Product(db.Document):
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    price = db.FloatField(required=True)

