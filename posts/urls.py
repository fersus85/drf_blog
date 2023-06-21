from django.urls import path

from posts.views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
