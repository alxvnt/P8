from django.urls import reverse
from django.test import TestCase
from .models import User, Category, Product, Commentary, CommentaryProduct
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password


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

    def test_missing_username(self):

        data = {"mail": "fake@gmail.com", "password": "123456",
                "first_name": "Jogn", "last_name": "smith"
                }

        response = self.client.post(reverse("enregistrement"), data=data, follow=True,
                                    HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertTrue(response.status_code, 200)
        try:
            User.objects.create_user(username=None, email="fake@gmail.com", password="123456")
        except ValueError:
            self.assertEqual(True, True)
        except:
            self.assertEqual(True, False)

    def test_missing_password(self):

        data = {"username": "test", "mail": "fake@gmail.com",
                "first_name": "Jogn", "last_name": "smith"
                }

        response = self.client.post(reverse("enregistrement"), data=data, follow=True,
                                    HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertTrue(response.status_code, 200)
        try:
            User.objects.create_user(username="test", email="fake@gmail.com", password=None)
        except ValueError:
            self.assertEqual(True, True)
        except:
            self.assertEqual(True, False)


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


class UserFonctionTest(TestCase):

    def setUp(self):
        cat = Category.objects.create(
            name='Pizza',
        )

        self.prod1 = Product.objects.create(
            name='test1',
            nutrition_grade='d',
            rep_nutritionnel='https://static.openfoodfacts.org/images/products/376/020/test1',
            img='https://static.openfoodfacts.org/images/products/376/020/616/0102/test1.11.full.jpg',
            url='https://fr.openfoodfacts.org/produit/3760206160102/test1',
            category=Category.objects.get(name=cat))

        self.prod2 = Product.objects.create(
            name='test2',
            nutrition_grade='b',
            rep_nutritionnel='https://static.openfoodfacts.org/images/products/376/020/test2',
            img='https://static.openfoodfacts.org/images/products/376/020/616/0102/test2.11.full.jpg',
            url='https://fr.openfoodfacts.org/produit/3760206160102/test2',
            category=Category.objects.get(name=cat))

        self.prod3 = Product.objects.create(
            name='test3',
            nutrition_grade='a',
            rep_nutritionnel='https://static.openfoodfacts.org/images/products/376/020/test3',
            img='https://static.openfoodfacts.org/images/products/376/020/616/0102/test3.11.full.jpg',
            url='https://fr.openfoodfacts.org/produit/3760206160102/test3',
            category=Category.objects.get(name=cat))

        data = {"username": "test", "mail": "fake@gmail.com", "password": "123456",
                "first_name": "Jogn", "last_name": "smith"
                }

        User.objects.create_user(username="test",
                                 email="fake@gmail.com",
                                 last_name="Jogn",
                                 first_name="smith",
                                 password="123456"
                                )

        self.users = User.objects.get(username="test")

        self.com1 = Commentary.objects.create(com="Vraiment bon", com_date=date.today())
        self.com2 = Commentary.objects.create(com="Delicieux", com_date=date.today())
        self.com3 = Commentary.objects.create(com="Je ne recommande pas", com_date=date.today())

    def test_com(self):

        com1 = Commentary.objects.get(id=1)
        expected_product_name = f'{com1.com}'

        self.assertEqual(expected_product_name, 'Vraiment bon')

    def test_prod_com(self):

        prod1 = Product.objects.get(name="test3")
        com1 = Commentary.objects.create(com="Vraiment bon", com_date=date.today())
        com2 = Commentary.objects.create(com="Delicieux", com_date=date.today())

        com_prod1 = CommentaryProduct.objects.create(prod=prod1, com=com1)
        com_prod2 = CommentaryProduct.objects.create(prod=prod1, com=com2)

        list_com = CommentaryProduct.objects.filter(prod=prod1)

        com_test = list_com[1].com
        self.assertEqual(com_test.com, "Delicieux")

    def test_com_username(self):
        self.username = "Dupont"
        char = "Horrible"

        com = (self.username + " : " + char)
        com1 = Commentary.objects.create(com=com, com_date=date.today())
        self.assertEqual(com1.com, "Dupont : Horrible")

    # def test_connexion(self):
    #
    #     self.username = "test"
    #     self.password = "123456"
    #
    #     data = {"username": self.username, "password": self.password}
    #     response = self.client.post(reverse('connexion'), data=data, follow=True, HTTP_X_REQUESTED='XMLHttpRequest')
    #     self.assertEqual(response.status_code, 200)

    def test_fail_connexion(self):

        self.username = "tset"
        self.password = "654321"

        data = {"username" : self.username, "password" : self.password}
        response = self.client.post(reverse('connexion'),data= data , follow=True, HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_nutriscore(self):

        self.assertEqual(self.prod3.nutrition_grade, "a")


class LoginTest(TestCase):

    def setUp(self):
        self.new_user = User.objects.create(email="nouveau@test.com", password="new_password")

    def test_login(self):
        self.logging = authenticate(email="nouveau@test.com", password="new_password")
        if self.logging:
            response = self.client.get(self.logging)
            self.assertEqual(response['email'], "nouveau@test.com")
