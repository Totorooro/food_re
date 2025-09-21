from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipesView.as_view(), name="home"),
]

