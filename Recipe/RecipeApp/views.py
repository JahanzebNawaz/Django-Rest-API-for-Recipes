from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView

from .models import Step, Ingredient, Recipe
from .serializers import StepSerializer, IngredientSerializer , RecipeSerializer
# Create your views here.


class StepsView(ListAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class IngredientView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeView(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

