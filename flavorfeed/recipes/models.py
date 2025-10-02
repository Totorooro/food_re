from django.db import models
from unidecode import unidecode
from django.utils.text import slugify



class Dish(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Легко'),
        ('medium', 'Средне'),
        ('hard', 'Сложно'),
    ]


    name = models.CharField(max_length=50, verbose_name='Название блюда')
    descr = models.TextField(max_length=150, verbose_name='Описание блюда', blank=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    photo = models.ImageField(upload_to='dishes/',  null=True, blank=True, verbose_name='Фотография блюда')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    cooking_time = models.IntegerField(verbose_name='Время приготовления')
    dish_price = models.IntegerField(verbose_name='Стоимость блюда')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, verbose_name='Сложность приготовления')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='cats', verbose_name="Категория")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(str(self.name)))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюд'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(str(self.name)))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'