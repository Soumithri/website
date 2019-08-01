from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    # Generic class based view for displaying all the posts

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    # Generic class based view for retrieving all the posts

    queryset = Post.objects.all()
    serializer_class = PostSerializer
