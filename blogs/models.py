from django.db import models
from ckeditor.fields import RichTextField 

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    link=models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    


class Subscription(models.Model):
    email = models.EmailField(max_length=200, null=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email