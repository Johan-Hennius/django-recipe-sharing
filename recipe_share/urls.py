from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', include('recipe_share_app.urls')),
    path('recipes/', include('recipes.urls'))
]
