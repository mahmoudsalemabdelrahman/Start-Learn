from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.


def validate_image_dimensions(image):
    img = Image.open(image)
    width, height = img.size

    if width < 1000 or height < 500:
        raise ValidationError("Image dimensions should be at least 1000px wide and 500px tall.")



class PageBase(models.Model):
    title = models.CharField( max_length=150)
    sub_title = models.CharField( max_length=250)
    bg_image = models.ImageField( upload_to='images/%Y%m%d', validators=[validate_image_dimensions])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)


    class Meta:
        abstract = True


    def __str__(self):
        return self.title
    
    

class HomePage(PageBase):
    pass

class AboutPage(PageBase):
    description = models.TextField()
    


    



class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT =('DF','DRAFT')
        PUBLISHED = ('PUB','PUBLISHED')


    title = models.CharField( max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, related_name=("author"), on_delete=models.CASCADE)
    body = models.TextField()
    bg_image = models.ImageField( upload_to='images/%Y%m%d/background_images',null=True,blank=True)
    post_image = models.ImageField(upload_to='images/%Y%m%d/post_images')
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField( max_length=10, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']

        indexes = [
            models.Index(fields=['-publish'])
            ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name=("comments"), on_delete=models.CASCADE)
    name = models.CharField( max_length=150)
    email = models.EmailField( max_length=254)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    active = models.BooleanField( default=False)

    class Meta:
        ordering = ['-created_at']

        indexes = [
            models.Index(fields=['-created_at'])
            ]

    def __str__(self):
        return f"Comment by {self.name} on post {self.post}"
  