from django.urls import path
from . import views


urlpatterns = [
    path('step/', views.StepsView.as_view(), name='steps'),
    # path('step/<int:pk>', views.StepsView.as_view(), name='steps'),
    path('ingredient/', views.IngredientView.as_view(), name='ingredient'),
    path('recipe/', views.RecipeView.as_view(), name='recipe'),
    path('recipe/<int:pk>/', views.RecipeDetailsView.as_view(), name='recipes')

]