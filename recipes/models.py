from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Create your models here.
MEAL_TYPES = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner')
)

class Recipe(models.Model):
    """
    A model to create and manage recipes
    """
    user = models.ForeignKey(User, related_name="recipe_owner", on_delete=models.CASCADE)
    title = models.Charfield(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to='recipes/',
        force_format='WEBP',
        blank=False,
        null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default='breakfast')