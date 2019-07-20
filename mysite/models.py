from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Model representing a project"""
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
