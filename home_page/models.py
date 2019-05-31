from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField()
    location = models.TextField()

class Book(models.Model):
    name = models.TextField()
    publish_date = models.DateField()
    author = models.ManyToManyField(Author)

