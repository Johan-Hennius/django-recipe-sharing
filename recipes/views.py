from django.views.generic import CreateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm


# Create your views here.
class Recipes(ListView):
    """
    View all recipes
    """

    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"


class RecipeDetail(DetailView):
    """
    View a single recipe
    """

    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Add recipe to site
    """

    template_name = "recipes/add_recipe.html"
    model = Recipe
    success_url = "/recipes/"
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)
