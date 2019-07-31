from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # Serializer for the model - Posts

    class Meta:
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        model = Post
