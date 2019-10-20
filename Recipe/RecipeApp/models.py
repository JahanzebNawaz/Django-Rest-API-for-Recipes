from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Step(models.Model):
    step_text = models.CharField(max_length=100, null=False, verbose_name='Steps')

    class Meta:
        verbose_name_plural = 'Steps'

    def __str__(self):
        return self.step_text


class Ingredient(models.Model):
    text = models.CharField(max_length=200, null=False, verbose_name='Text')

    class Meta:
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.text


class Recipe(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name='Name')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    step_text = models.ForeignKey(Step, on_delete=models.CASCADE, verbose_name='Steps')
    text = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name='Text')

    class Meta:
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.name

