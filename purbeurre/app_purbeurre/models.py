from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=50, unique= True)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    rep_nutritionnel = models.URLField(null=True)
    nutrition_grade = models.CharField(max_length=1, null=True)
    url = models.URLField()
    img = models.URLField()

    def __str__(self):
        return str(self.name)


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


class SavedSubstitute(models.Model):
    product = models.ForeignKey('product', on_delete=models.CASCADE, verbose_name="related prod",related_name='fav_prod')
    substitute = models.ForeignKey('product', on_delete=models.CASCADE, verbose_name="related sub", related_name='fav_sub')
    user = models.ForeignKey('user', on_delete=models.CASCADE)