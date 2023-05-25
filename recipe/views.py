from django.shortcuts import render
from .models import Recipe


def main(request):
    recipes = Recipe.objects.filter(created_at__year=2023)
    return render(request, 'main.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

