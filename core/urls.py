from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('create/', views.ArticleCreate.as_view()),
    path('<str:pk>/', views.ArticleSingle.as_view()),
    
]