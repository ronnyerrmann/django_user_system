import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    """
    Use the AbstractUser class so the login to the django admin page can be handled with this table
    - to login to the admin site, the Person must have is_staff=True set
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=128)

    @property
    def age(self) -> int:
        today = datetime.date.today()
        years = today.year - self.dob.year
        if (today - datetime.date(today.year, self.dob.month, self.dob.day)).days < 0:
            # The birthday this year hasn't happened yet
            years -= 1
        return years

