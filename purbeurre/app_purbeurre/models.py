from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    brand = models.ForeignKey('brand', on_delete=models.CASCADE)
    store = models.ManyToManyField('store', related_name='product')
    nutriscore = models.IntegerField()
    url = models.URLField()
    img = models.URLField()

    def __str__(self):
        return str(self.name)


class User(models.Model):
    pseudo = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


class SavedSubstitute(models.Model):
    product = models.ForeignKey('product', on_delete=models.CASCADE)
    substitute = models.IntegerField()
    user = models.ForeignKey('user', on_delete=models.CASCADE)