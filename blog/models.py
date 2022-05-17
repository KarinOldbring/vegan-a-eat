from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, 'Draft'), (1, 'Published'))

class Post(models.Model):
    """
    Model for the recipe
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    cooking_time = models.IntegerField(default=1,
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(120)
        ])
    ingredients = models.TextField()
    instructions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)


class Meta:
    ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
