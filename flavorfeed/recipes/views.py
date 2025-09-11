from django.views.generic import ListView
from .models import Dish, Category

class RecipesView(ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        queryset = Dish.objects.all()
        category_slug = self.request.GET.get('category')
        difficulty = self.request.GET.get('difficulty')

        if category_slug and category_slug != 'all':
            queryset = queryset.filter(cat__slug=category_slug)
        if difficulty and difficulty != 'all':
            queryset = queryset.filter(difficulty=difficulty)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context