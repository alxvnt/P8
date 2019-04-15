from app_purbeurre.models import Category, Product, User
from django.core.management.base import BaseCommand, CommandError
import requests
import json
import django

cats = [
    "biscuits et gâteaux", "pizzas", "pâtes à tartiner aux noisettes", "glaces",
    "chocolats", "sodas", "bonbons", "chips", "céréales", "fromages", "confitures",
    "jus de fruits", "desserts lactés", "soupes", "lasagnes", "miels",
    "galettes de céréales", "rillettes", "bières", "hummus", "brioches", "sandwichs"
]
nutriscore = ['A', 'B', 'C', 'D', 'E']

url = "https://fr.openfoodfacts.org/cgi/search.pl"

criteria = {
    "action": "process",
    "tagtype_0": "categories",
    "tag_contains_0": "contains",
    "tagtype_1": "nutrition_grades",
    "tag_contains_1": "contains",
    "page_size": "1",
    "json": "1",
}


class Command(BaseCommand):
    help = "Import openfoodfact data in project's database"

    def import_cats(self, cat):

        category, created = Category.objects.get_or_create(name= cat)
        category.save()

    def import_prod(self, data, category):

        for prod_data in data['products']:
            name = prod_data.get('product_name', None)
            category = Category.objects.get(name=category)
            rep_nutritionnel = prod_data.get('image_nutrition_url', None)
            nutrition_grade = prod_data.get('nutrition_grades', None)
            url = prod_data.get('url', None)
            img = prod_data.get('image_url', None)
            if category == None \
                    or name == None \
                    or len(name) > 50 \
                    or rep_nutritionnel == None \
                    or nutrition_grade == None or url == None or img == None:
                continue
            else:
                try:
                    prod, created = Product.objects.get_or_create(
                        name = name,
                        category = category,
                        rep_nutritionnel = rep_nutritionnel,
                        nutrition_grade = nutrition_grade,
                        url = url,
                        img = img,
                    )
                    if created:
                        prod.save()
                        print(prod.name)
                except Product.DoesNotExist:
                    raise CommandError("Product %s n'a pas été trouvé" % name)
                except django.db.utils.IntegrityError:
                    continue

    def handle(self, *args, **options):

        for c in cats:
            self.import_cats(c)
            criteria['tag_0'] = c
            for tag in nutriscore:
                criteria['tag_1'] = tag
                response = requests.get(url, params=criteria)
                products = response.json()

                self.import_prod(products, c)
