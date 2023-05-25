from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Створення тестових об'єктів рецептів
        Recipe.objects.create(title='Recipe 1', year=2023)
        Recipe.objects.create(title='Recipe 2', year=2022)
        Recipe.objects.create(title='Recipe 3', year=2023)

    def test_main_view(self):
        url = reverse('main')
        response = self.client.get(url)
        # Перевірка статусу відповіді
        self.assertEqual(response.status_code, 200)
        # Перевірка наявності всіх рецептів за 2023 рік у контексті
        self.assertEqual(len(response.context['recipes']), 2)

    def test_recipe_detail_view(self):
        recipe = Recipe.objects.first()  # Отримання першого рецепту
        url = reverse('recipe_detail', args=[recipe.id])
        response = self.client.get(url)
        # Перевірка статусу відповіді
        self.assertEqual(response.status_code, 200)
        # Перевірка, що отримано правильний рецепт у контексті
        self.assertEqual(response.context['recipe'], recipe)



