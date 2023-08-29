from rest_framework import viewsets
from blog.models import User, Keyword
from blog.serializers import UserSerializer, KeywordSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class KeywordView(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
