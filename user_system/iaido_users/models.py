import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    """
    Use the AbstractUser class so the login to the django admin page can be handled with this table
    - to login to the admin site, the Person must have is_staff=True set
    """
    # first_name = models.CharField(max_length=200)             # Use the object from base class
    # last_name = models.CharField(max_length=200)              # Use the object from base class
    # email = models.EmailField(unique=True)                    # Use the object from base class
    phone = models.CharField(max_length=20)
    dob = models.DateField("Date of birth")
    # username = models.CharField(max_length=200, unique=True)  # Use the object from base class
    # password = models.CharField(max_length=128)               # Use the object from base class


    @property
    def age(self) -> int:
        """ Use the date of birth in the database to calculate the age of the user
        """
        today = datetime.date.today()
        years = today.year - self.dob.year
        if (today - datetime.date(today.year, self.dob.month, self.dob.day)).days < 0:
            # The birthday this year hasn't happened yet
            years -= 1
        return years

    def save(self, *args, **kwargs):
        """ Before saving, hash the password, if necessary
        """
        password_needs_hash = True
        if self.pk:
            # Object already exists in the database, check for field changes
            original_obj = Person.objects.get(pk=self.pk)
            if self.password == original_obj.password:
                password_needs_hash = False
        if password_needs_hash:
            self.set_password(self.password)
        super().save(*args, **kwargs)
