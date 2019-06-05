from django.test import TestCase


class RegisterTest(TestCase):

    def test_uses_signup_page(self):
        response = self.client.get('/enregistrement/')
        self.assertEqual(response.status_code, 200)


class TestAPI(TestCase):

    def test_api(self):
        response = self.client.get('https://fr.openfoodfacts.org/produit/20711269/saucisson-cuit-a-l-ail-saint-alby')
        self.assertEqual(response.status_code, 200)