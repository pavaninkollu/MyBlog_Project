from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    
    
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    
    CATEGORY_CHOICES  = [
        ('Global', 'Python'),
        ('tech', 'Java'),
        ('Ai', 'Machine Learning'),
        ('other', 'Other'),
    ]
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True, blank=True)
    # category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, default=1)  # Add category here
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image=models.ImageField(upload_to='post_images/', blank=True, null=True)
    content=RichTextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    
    
    
    def save(self, *args, **kwargs):
        self.title = self.title.title()  # Convert title to Title Case
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.title
    
    
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text=models.TextField()
    created_At=models.DateTimeField(default=timezone.now)
    
    
    def __str__(self) -> str:
        return f'Comment by {self.author} on {self.post}'