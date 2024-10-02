from django.db import models


class Client(models.Model):
    name = models.CharField(
        blank=False,
        max_length=256,
        primary_key=False,
        unique=False,
        null=False,
        verbose_name="Name",
    )
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(
        blank=False,
        max_length=256,
        primary_key=False,
        unique=False,
null=False,
        verbose_name="Name",
    )
    price = models.FloatField(
        blank=False,
        primary_key=False,
        unique=False,
        null=False,
        verbose_name="Price",
    )
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=False,
        blank=False,
        max_length=256,
primary_key=False,
        unique=False,
        name="client_cart",
        verbose_name="Client",
    )
    products = models.ManyToManyField(
        Product,
        null=True,
        blank=True,
        primary_key=False,
        unique=False,
        name="products_cart",
        verbose_name="Products",
    )
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)