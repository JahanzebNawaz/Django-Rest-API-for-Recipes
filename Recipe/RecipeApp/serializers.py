from rest_framework import serializers
from .models import Step, Ingredient, Recipe


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'step_text')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'text')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'user', 'step_text', 'text')



