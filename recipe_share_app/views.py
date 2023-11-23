from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'recipe_share_app/index.html'