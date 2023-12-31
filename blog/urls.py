from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register(r'users', views.UserView)
router.register(r'keywords', views.KeywordView)
router.register(r'articles', views.ArticleView)
router.register(r'comments', views.CommentView)

urlpatterns = [
    path('', include(router.urls)),
    path('comments/article/<int:pk>/',
         views.ArticleView.as_view({'get': 'comments'})),
]
