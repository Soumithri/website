from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    # Serializer for the model - Posts

    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        models = Post
