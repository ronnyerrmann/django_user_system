import copy
from datetime import date
from unittest.mock import call, MagicMock, patch

from django.test import TestCase
from .models import Person


class Test_Person(TestCase):
    def setUp(self) -> None:
        Person.objects.create(
            first_name="foo", last_name="bar", email="a@b.c", phone="123", dob="1965-06-16", username="fooU",
            password="barP"
        )

    def test_password_hashed(self):
        person = Person.objects.get(username="fooU")

        self.assertTrue(person.password != "barP")
        self.assertEqual(date(1965, 6, 16), person.dob)

    def test_save_no_password_change(self):
        person = Person.objects.get(username="fooU")
        person.last_name = "baz"
        old_password = copy.copy(person.password)
        person.set_password = MagicMock()

        person.save()

        self.assertEqual(old_password, person.password)
        person.set_password.assert_not_called()

    def test_save_password_change(self):
        person = Person.objects.get(username="fooU")
        person.password = "new"
        person.set_password = MagicMock()

        person.save()

        person.set_password.assert_called_once_with("new")

    def test_age(self):
        person = Person.objects.get(username="fooU")

        with patch("iaido_users.models.datetime.date") as mock_date:
            # This is required instead of a @patch
            mock_date.today.return_value = date(2023, 6, 7)
            mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

            self.assertEqual(57, person.age)

