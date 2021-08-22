from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.userRegister, name='user-register'),
    path('login/', views.userlogin, name='user-login'),
    path('edit/', views.userEdit, name='user-edit'),
    path('logout/', views.userLogout, name='user-logout'),
    path('settings/<str:pk>/', views.settings, name='settings'),
]
