from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from blog.models import Article, Comment, Keyword
from blog.serializers import (ArticleSerializer, CommentSerializer,
                              KeywordSerializer, UserSerializer)


class WriteOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST' or (request.user and request.user.is_authenticated)


class UserView(viewsets.ModelViewSet):
    permission_classes = [WriteOrAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class KeywordView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class ArticleView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        article = self.get_object()
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
