from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import CASCADE
from django.utils.safestring import mark_safe
from rest_framework.reverse import reverse

from core.models import User


class CustomModelMixin(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=150, verbose_name="Название")
    email = models.EmailField()
    country = models.CharField(max_length=200, verbose_name="Страна", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="Город", blank=True, null=True)
    street = models.CharField(max_length=80, verbose_name="Улица", blank=True, null=True)
    house = models.IntegerField(verbose_name="Номер дома", blank=True, null=True)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)


class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    product_model = models.CharField(max_length=100, verbose_name="Модель")
    release_date = models.DateField(auto_now_add=True, verbose_name="Дата выпуска")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


class FactoryStore(CustomModelMixin):
    products = models.ManyToManyField(
        Products,
        verbose_name="Продукты"
    )

    class Meta:
        verbose_name = "Фабрика"
        verbose_name_plural = "Фабрики"

    def __str__(self):
        return self.title


class Retailer(CustomModelMixin):
    products = models.ManyToManyField(
        Products,
        verbose_name="Продукты"
    )
    supplier = models.ForeignKey(
        FactoryStore,
        on_delete=CASCADE,
        verbose_name="Поставщик"
    )
    credit = models.IntegerField(verbose_name="Задолженность")

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    def __str__(self):
        return self.title


class Entrepreneur(CustomModelMixin):
    products = models.ManyToManyField(Products, verbose_name="Продукты")
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    supplier = GenericForeignKey('content_type', 'object_id')
    credit = models.IntegerField(verbose_name="Задолженность")

    objects = models.Manager()

    class Meta:
        ordering = ['created']
        verbose_name = 'Предприниматель'
        verbose_name_plural = 'Предприниматели'

    def __str__(self):
        return self.title
