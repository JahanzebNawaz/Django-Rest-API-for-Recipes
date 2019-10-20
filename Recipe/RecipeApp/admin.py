from django.contrib import admin
from .models import Step, Ingredient, Recipe
# Register your models here.


class Steps(admin.ModelAdmin):
    list_display = ['step_text']


admin.site.register(Step, Steps)


class Ingredients(admin.ModelAdmin):
    list_display = ['text']


admin.site.register(Ingredient, Ingredients)


class Recipes(admin.ModelAdmin):
    list_display = ['name', 'user']


admin.site.register(Recipe, Recipes)