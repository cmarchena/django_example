from django.db import models
from django.contrib.auth.models import User
STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    def __str__(self):
        return self.title
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    def __str__(self) -> str:
        return self.user.username