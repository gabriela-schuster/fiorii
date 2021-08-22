from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'body_text']
        widgets = {
            'body_text': forms.Textarea
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input', 'spellcheck': 'false'})
