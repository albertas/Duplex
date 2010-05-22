from project.recipes.models import Recipe, RecipeType, Cusine, CookingType, \
Complexity
from django.contrib import admin

admin.site.register(Recipe)
admin.site.register(RecipeType)
admin.site.register(Cusine)
admin.site.register(CookingType)
admin.site.register(Complexity)