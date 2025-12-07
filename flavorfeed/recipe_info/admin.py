from django.contrib import admin
from recipes.models import Dish
from recipes.admin import DishAdmin as ExistingDishAdmin 
from .models import DishIngredient, Step, Ingredient



@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']



class DishIngredientInline(admin.TabularInline):
    model = DishIngredient
    extra = 1  
    autocomplete_fields = ['ingredient']  


class StepInline(admin.TabularInline):
    model = Step
    extra = 1
    fields = ['number', 'description']



admin.site.unregister(Dish)

@admin.register(Dish)
class DishAdmin(ExistingDishAdmin):
    inlines = [DishIngredientInline, StepInline]