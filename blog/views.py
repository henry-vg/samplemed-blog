from rest_framework import viewsets
from blog.models import User, Keyword, Article, Comment
from blog.serializers import UserSerializer, KeywordSerializer, ArticleSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class KeywordView(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        article = self.get_object()
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
