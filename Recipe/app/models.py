from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length= 50)

    class Meta:
        verbose_name = 'Users'
        
    def __str__(self):
        return self.username



class StepModel(models.Model):
    step_text = models.CharField( max_length=100, null= False)

    class Meta:
        verbose_name = 'Step'
    
    def __str__(self):
        return self.step_text

class IngredientModel(models.Model):
    text = models.CharField(max_length= 100,  null= False )

    class Meta:
        verbose_name = 'Intgredient'
    
    def __str__(self):
        return self.text

class RecipeModel(models.Model):
    name = models.CharField(null= False, max_length=100)
    user = models.OneToOneField(UserModel, primary_key=True, on_delete=models.CASCADE)
    step = models.ForeignKey(StepModel, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(IngredientModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Recipe'

    def __str__(self):
        return self.name

    


''' 1. Design the User Model with username(unique field), email(unique field), first_name,
    last_name,m password. (You can use the django inbuilt user model)
    2. Design A Step Model with step_text(string field, not null), Many to One relationship with
    Recipe
    3. Design An Ingredient Model with text(not null, string), Many to One relationship with
    Recipe
    4. Design A Recipe Model with name(string, not null), Foreign Key to User table(one to one
    relationship), One to Many relationship with Step and Ingredient Model
'''
