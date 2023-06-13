from django.contrib.auth.backends import ModelBackend
from .models import Person


class PersonBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """ Use the Person table to login to the admin page
        """
        try:
            person = Person.objects.get(username=username)
        except Person.DoesNotExist:
            return None
        if person.check_password(password):
            return person

        return None