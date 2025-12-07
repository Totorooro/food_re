from django.views.generic import DetailView
from recipes.models import Dish, Category
from .models import Ingredient, DishIngredient, Step

class DishDetailView(DetailView):
    model = Dish
    template_name = "recipe_info/dish_details.html"
    context_object_name = 'dish'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.dish_ingredients.all()
        context['steps'] = self.object.steps.all().order_by('number')
        return context