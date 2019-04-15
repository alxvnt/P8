from django.urls import reverse
from django.test import TestCase
from .models import User
from django.contrib.auth.models import User
from purbeurre import AppConfig


class IndexPageTestCase(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class RegisterTest(TestCase):

    def test_register(self):
        data = { "username" : "test", "email" : "fake@gmail.com", "password" : "123456",
                 "first_name" : "Jogn", "last_name" : "smith"
                 }

        response = self.client.post(reverse("enregistrement"), data=data, follow= True,
                                    HTTP_X_REQUESTED='XMLHttpRequest')
        fake_user = User.objects.get(email="fake@gmail.com")
        self.assertTrue(fake_user)
        self.assertRedirects(response, reverse("connexion"), status_code=302, target_status_code=200)