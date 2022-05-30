"""from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login


class userTest(TestCase):
	def test_user_is_created_and_can_login(self):
		new_user = User.objects.create(
			username='test_user',
			password='dfgs435!34#dfA'
		)
		req = self.client.get(reverse('all-articles'))
		login(req, new_user)
"""		
