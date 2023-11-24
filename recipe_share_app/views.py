from django.views.generic import ListView
from recipes.models import Recipe

class Index(ListView):
    template_name = 'recipe_share_app/index.html'
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self):
        return self.model.objects.all()[:3]