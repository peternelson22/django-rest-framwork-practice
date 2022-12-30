from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('article', views.ArticleModelViewSet, basename='article') # Call any of the classes to use

urlpatterns = [
    path('', include(router.urls)),
    path('<str:pk>', include(router.urls)),
    # path('', views.ArticleList.as_view()),
    # path('', views.ArticleGenericView.as_view()), # GenericView
    # path('create/', views.ArticleCreate.as_view()),
    # path('<str:pk>/', views.ArticleSingle.as_view()),  
    # path('<str:pk>/', views.ArticleEditGenericView.as_view()), # GenericView


    
]