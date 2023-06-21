from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from posts.models import Post
from posts.serializers import PostSerializer


# Create your views here.
class PostList(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
