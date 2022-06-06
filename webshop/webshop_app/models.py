from datetime import datetime
import uuid as uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='webshop_app/static/media/profiles')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    country = CountryField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)


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


class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(decimal_places=2, max_digits=6)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    order_date = models.DateTimeField(default=datetime.now)
    note = models.TextField(null=True, blank=True, max_length=1000)
    cancelled = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
