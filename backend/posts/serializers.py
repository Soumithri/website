from rest_framework import serializers
from .models import Post, Project, Author


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # Serializer for the model - Posts

    class Meta:
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        model = Post


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    # Serializer for the model - Posts

    class Meta:
        fields = ['id', 'title', 'description', 'technology', 'github_link', 'sample_doc', 'project_img']
        model = Project


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    # Serializer for the model - Posts

    class Meta:
        fields = ['id', 'first_name', 'last_name', 'description', 'github_link', 'linkedIn_link', 'image', 'resume']
        model = Author
