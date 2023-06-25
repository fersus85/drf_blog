from django.contrib.auth import get_user_model
from .permissions import IsAuthorOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework import viewsets
from posts.models import Post
from posts.serializers import PostSerializer, UserSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



