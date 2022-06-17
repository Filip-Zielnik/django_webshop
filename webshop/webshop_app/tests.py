from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestUser(TestCase):

    def test_login(self):
        user = User.objects.create(username='test_user')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='test_user', password='12345')
        self.assertTrue(logged_in)
