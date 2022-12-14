from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    post model with category section
    """
    category = [
        ('gear', 'gear'),
        ('rider', 'rider'),
        ('food', 'food'),
        ('exercise', 'exercise'),
        ('horse', 'horse'),
        ('selfcare', 'selfcare'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=category, default='horse')
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    image_filter = models.CharField(
        max_length=32, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
