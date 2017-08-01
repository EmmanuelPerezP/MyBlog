from django.db import models
from django.urls import reverse
# Used to generate URLs by reversing the URL patterns


class Post(models.Model):
    """
    Class representing a blog post
    """
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    bodyHTML = models.TextField()
    dateCreated = models.DateTimeField()
    postStatus = models.BooleanField(default=False)
    visits = models.BigIntegerField()
    likes = models.BigIntegerField()
    datePublished = models.DateTimeField()
    dateLastUpdated = models.DateTimeField()

    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        """
        String representing the model
        """
        return self.title

    def get_absolute_url(self):
        """
        return the url to access this particular post
        """
        return reverse('post-detail', args=[str(self.id)])


class Category(models.Model):
    """
    Categorias de cada Post
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        """
        String representing the model
        """
        return self.name


class Tag(models.Model):
    """
    Tags de cada post ManyToMany
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        """
        Sidtring representing the model
        """
        return self.name
