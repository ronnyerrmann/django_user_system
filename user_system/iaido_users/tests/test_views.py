import datetime

from django.test import TestCase
from django.urls import reverse
from iaido_users.models import Person


class Test_index(TestCase):

    def setUp(self):
        Person.objects.create(
            first_name="foo", last_name="bar", email="a@b.c", phone="123", dob="1965-06-16", username="fooU",
            password="barP"
        )
        Person.objects.create(
            first_name="foo2", last_name="bar2", email="a@b.c", phone="123", dob=datetime.date.today(), username="foo2U",
            password="barP", is_staff=True
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('index'))

        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(302, response.status_code)
        self.assertTrue(response.url.startswith('login/'))

    def test_admin_forbidden_if_logged_in_but_not_correct_permission(self):
        login = self.client.login(username='fooU', password='barP')
        response = self.client.get(reverse('admin:index'))

        self.assertEqual(302, response.status_code)
        self.assertTrue(response.url.startswith('/admin/login/'))

    def test_admin_logged_in_with_permission(self):
        login = self.client.login(username='foo2U', password='barP')
        response = self.client.get(reverse('admin:index'))

        self.assertEqual(200, response.status_code)

    def test_logged_in(self):
        login = self.client.login(username='fooU', password='barP')
        response = self.client.get(reverse('index'))

        self.assertEqual(200, response.status_code)
        # also contains the two users automatically created
        self.assertEqual(4, len(response.context["objects"]))

    def test_logged_in_filter_first_name(self):
        login = self.client.login(username='fooU', password='barP')
        response = self.client.get('/iaido/?first_name=oo')

        self.assertEqual(2, len(response.context["objects"]))

    def test_logged_in_filter_first_name_last_name(self):
        login = self.client.login(username='fooU', password='barP')
        response = self.client.get('/iaido/?first_name=oo&last_name=bar2')

        self.assertEqual(1, len(response.context["objects"]))

    def test_logged_in_filter_last_name_age(self):
        login = self.client.login(username='fooU', password='barP')
        response = self.client.get('/iaido/?last_name=ar&age=0')

        self.assertEqual(1, len(response.context["objects"]))