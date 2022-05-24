from django.test import TestCase
from django.urls import reverse


class ArticleURLsTest(TestCase):
	def test_pytest_is_ok(self):
		print('ok') # -rP to show out

	def test_recipe_home_url_is_correct(self):
		url = reverse('all-articles')
		self.assertEqual(url, '/')

	def test_single_article_url_is_correct(self):
		url = reverse('single-article', args=('2d72f5b3-cf5a-4567-beb9-c3cbb13aca03',))
		self.assertEqual(url, '/article/2d72f5b3-cf5a-4567-beb9-c3cbb13aca03/')
