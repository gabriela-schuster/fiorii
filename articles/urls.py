from django.urls import path
from . import views

urlpatterns = [
    path('', views.allArticles, name='all-articles'),
    path('article/<str:pk>/', views.singleArticle, name='single-article'),

    path('edit/<str:pk>/', views.editArticle, name='edit-article'),
    path('delete/<str:pk>/', views.deleteArticle, name='delete-article'),
    path('create/', views.createArticle, name='create-article'),
]
