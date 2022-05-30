from django.test.testcases import TestCase
from django.core.exceptions import ValidationError
from parameterized import parameterized

from articles.models import Article


class articleModelTest(TestCase):
	def setUp(self) -> None:
		self.article = Article.objects.create(
			title='test article',
			description='test',
			body_text='lorem ipsum dolor sit amet',
		)
		return super().setUp()

	def test_article_title_raises_error_if_greater_than_100_chars(self):
		self.article.title = 'a' * 101
		with self.assertRaises(ValidationError):
			self.article.full_clean()

	@parameterized.expand([
			('title', 100),
			('description', 200),
			('body_text', 5000),
		])
	def test_article_fields_max_length(self, field, max_len):
		setattr(self.article, field, 't' * (max_len + 1))
		with self.assertRaises(ValidationError):
			self.article.full_clean()

