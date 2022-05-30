from django.test import TestCase
from django.urls import reverse, resolve
from articles import views
from articles.models import Article


class ArticleViewsTest(TestCase):
	# def setup(self) -> None:
	#   create fixture here, as example
	# 	return super().setUp()

	# def tearDown(self) -> None:
	# 	return super().tearDown()
	
	# Setup is called here
	def test_articles_home_views_function_is_correct(self):
		view = resolve(reverse('all-articles')).func
		self.assertIs(view, views.allArticles)
	# Teardown here
		
	def test_articles_home_returns_status_code_200(self):
		response = self.client.get(reverse('all-articles'))
		self.assertEqual(response.status_code, 200)

	def test_articles_home_view_loads_correct_template(self):
		response = self.client.get(reverse('all-articles'))
		self.assertTemplateUsed(response, 'all-articles.html')

	def test_articles_home_template_loads_articles(self):
		article = Article.objects.create(
			title='test article',
			description='test',
			body_text='lorem ipsum dolor sit amet',
		)
		response = self.client.get(reverse('all-articles'))
		self.assertEqual(len(response.context['articles']), 1)

	def test_articles_home_template_is_rendering_articles(self):
		article = Article.objects.create(
			title='test article',
			description='test',
			body_text='lorem ipsum dolor sit amet',
		)
		response = self.client.get(reverse('all-articles'))
		content = response.content.decode('utf-8')
		self.assertIn('test article', content)

	def test_single_article_view_returns_404_if_no_article(self):
		response = self.client.get(reverse('single-article', args=('2d72f5b3-cf5a-4567-beb9-c3cbb13aca04',)))
		self.assertEqual(response.status_code, 404)

