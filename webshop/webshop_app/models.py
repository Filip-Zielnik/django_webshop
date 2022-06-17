from datetime import datetime
import uuid as uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField

from django.shortcuts import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()

    def __str__(self):
        return str(self.user)


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = CountryField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    picture = models.ImageField(upload_to='webshop_app/static/media/products', null=True, blank=True)
    available = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.product

    def get_add_to_cart_url(self) :
        return reverse("core:add-to-cart", kwargs={
            "pk": self.pk
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            "pk": self.pk
        })


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    order_date = models.DateTimeField(default=datetime.now)
    note = models.TextField(null=True, blank=True, max_length=1000)
    cancelled = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
