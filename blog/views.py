from rest_framework import viewsets
from blog.models import User
from blog.serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer