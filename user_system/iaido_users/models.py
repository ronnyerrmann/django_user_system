import datetime
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dob = models.Field("Date of Birth")
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, default="guest")

    def age(self, date):
        today = datetime.date.today()
        years = today.year - date.year
        if (today - datetime.date(today.year, date.month, date.day)).days < 0:
            # The birthday this year hasn't happened yet
            years -= 1
        return years
