from django.test import TestCase
from django.urls import reverse, resolve
from articles import views


class RecipeViewsTest(TestCase):
	def test_articles_home_views_function_is_correct(self):
		view = resolve(reverse('all-articles')).func
		self.assertIs(view, views.allArticles)

	def test_articles_home_returns_status_code_200(self):
		response = self.client.get(reverse('all-articles'))
		self.assertEqual(response.status_code, 200)

	def test_articles_home_view_loads_correct_template(self):
		response = self.client.get(reverse('all-articles'))
		self.assertTemplateUsed(response, 'all-articles.html')
