from django.db import models
from users.models import Profile
import uuid


class Article(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body_text = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
