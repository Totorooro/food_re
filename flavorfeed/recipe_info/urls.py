# recipe_info/urls.py
from django.urls import path
from .views import DishDetailView

app_name = 'recipe_info'

urlpatterns = [
    path('<slug:slug>/', DishDetailView.as_view(), name='dish_detail'),
]