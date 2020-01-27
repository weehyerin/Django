from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #num_stars = models.IntegerField()