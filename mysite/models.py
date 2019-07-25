from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Model representing a Project"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    github_link = models.URLField(max_length=250, blank=True, null=True)
    sample_doc = models.FileField(blank=True, null=True, upload_to="docs/")
    cover_image = models.ImageField(blank=True, null=True, upload_to="images/")

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('project_detail', args=[str(self.id)])


class Author(models.Model):
    """Model representing the author of the website"""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    description = models.TextField()
    github_link = models.URLField(max_length=250, blank=True, null=True)
    linkedIn_link = models.URLField(max_length=250, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    resume = models.FileField(blank=True, null=True, upload_to="docs/")

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
