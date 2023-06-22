from .permissions import IsAuthorOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from posts.models import Post
from posts.serializers import PostSerializer


# Create your views here.
class PostList(CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
