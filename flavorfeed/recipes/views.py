from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Dish


class RecipesView(ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'dishes'



    def get_queryset(self):
        return Dish.objects.all()