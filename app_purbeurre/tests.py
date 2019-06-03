from django.urls import reverse
from django.test import TestCase
from .models import User, Category, Product
from django.contrib.auth.models import User


class IndexPageTestCase(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class RegisterTest(TestCase):

    def test_register(self):
        data = { "username" : "test", "mail" : "fake@gmail.com", "password" : "123456",
                 "first_name" : "Jogn", "last_name" : "smith"
                 }

        response = self.client.post(reverse("enregistrement"), data=data, follow= True,
                                    HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertTrue(response.status_code, 200)
        fake_user = User.objects.create_user(username="test", email="fake@gmail.com", password="123456")

        self.assertTrue(fake_user.username, "test")

        self.assertRedirects(response, reverse("connexion"), status_code=200, target_status_code=200)


class ProductTest(TestCase):

    def setUp(self):
        cat = Category.objects.create(
            name='Pizza',
        )

        Product.objects.create(
            name='pizza kebab',
            nutrition_grade='d',
            rep_nutritionnel='https://static.openfoodfacts.org/images/products/376/020/616/0102/ingredients_fr.12.full.jpg',
            img='https://static.openfoodfacts.org/images/products/376/020/616/0102/front_fr.11.full.jpg',
            url='https://fr.openfoodfacts.org/produit/3760206160102/yaourt-artisanal-noix-de-coco-ibaski',
            category=Category.objects.get(name=cat))

    def test_add_product(self):
        product = Product.objects.get(id=1)
        expected_product_name = f'{product.name}'

        self.assertEqual(expected_product_name, 'pizza kebab')