from django.test import TestCase

class RegisterTest(TestCase):

    def test_uses_signup_page(self):
        response = self.client.get('/enregistrement/')
        self.assertEqual(response.status_code, 200)
