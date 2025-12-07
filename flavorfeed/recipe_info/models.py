from django.db import models
from recipes.models import Dish


class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название ингредиента")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игредиент'
        verbose_name_plural = 'Ингредиенты'


class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50, verbose_name="Количество", help_text="например: 400 г, 3 шт, 1 ч.л.")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.amount} {self.ingredient}"
    

class Step(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='steps')
    number = models.PositiveSmallIntegerField(verbose_name="Номер шага")
    description = models.TextField(verbose_name="Описание шага")

    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'
        ordering = ['id']