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

class ProductTest(TestCase):

    def setUp(self):
        cat = Category.objects.create(
            name_cat='Pizza',
        )

        Product.objects.create(
            name_prod='pizza kebab',
            nutrition_grade='d',
            rep_nutritionnel='https://static.openfoodfacts.org/images/products/376/020/616/0102/ingredients_fr.12.full.jpg',
            image='https://static.openfoodfacts.org/images/products/376/020/616/0102/front_fr.11.full.jpg',
            url='https://fr.openfoodfacts.org/produit/3760206160102/yaourt-artisanal-noix-de-coco-ibaski',
            category=Category.objects.get(name_cat=cat))

    def test_add_product(self):
        product = Product.objects.get(id=1)
        expected_product_name = f'{product.name_prod}'

        self.assertEqual(expected_product_name, 'test product')