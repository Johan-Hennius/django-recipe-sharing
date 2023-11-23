from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm

# Create your views here.
class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Add recipe to site
    """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    success_url = '/recipes/'
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)