from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):
    """
    Модель Продукт
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255,
                            verbose_name='Название продукта',
                            blank = False)
    number = models.IntegerField(null=True,
                                     default=None,
                                     verbose_name='Колличество блюд')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'product'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Рецепт
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255,
                            verbose_name='Название рецепта',
                            blank=False)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        db_table = 'recipe'

    def __str__(self):
        return self.name


class Structure(models.Model):
    """
    Состав
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    Product = models.ForeignKey(Product,
                  on_delete=models.DO_NOTHING,
                  verbose_name='Продукт')
    Weight = models.IntegerField(null=True,
                                 default=None,
                                 verbose_name='Вес')
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.DO_NOTHING,
                               verbose_name='Рецепт')

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Составы'
        db_table = 'structure'

    def __str__(self):
        return str(self.uuid)




