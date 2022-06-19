from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.TextField()
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField