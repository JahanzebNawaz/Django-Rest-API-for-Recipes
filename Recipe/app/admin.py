from django.contrib import admin
from .models import RecipeModel, StepModel, IngredientModel, UserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(StepModel)
admin.site.register(IngredientModel)
admin.site.register(RecipeModel)