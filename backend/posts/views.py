from rest_framework import generics

from .models import Post, Project, Author
from .serializers import PostSerializer, ProjectSerializer, AuthorSerializer


class PostList(generics.ListAPIView):
    # Generic class based view for displaying all the posts

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    # Generic class based view for retrieving all the posts

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProjectList(generics.ListAPIView):
    # Generic class based view for displaying all the posts

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveAPIView):
    # Generic class based view for retrieving all the posts

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class AuthorDetail(generics.RetrieveAPIView):
    # Generic class based view for retrieving all the posts

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
