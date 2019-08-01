from django.db import models


class Post(models.Model):
    # Model for the Post object
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation for the model - Post
        return self.title
