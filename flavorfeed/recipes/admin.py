from django.contrib import admin
from .models import Dish, Category


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_time', 'dish_price', 'difficulty', 'cat')
    fields = ('name', 'descr', 'photo', 'cooking_time', 'dish_price', 'difficulty', 'cat')
    list_display_links = ('name',)
    list_editable = ['dish_price', 'difficulty', 'cat', 'cooking_time']
    list_per_page = 10
    ordering = ['id']
    search_fields = ['name__icontains']
    list_filter = ['cat', 'difficulty']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ['id']