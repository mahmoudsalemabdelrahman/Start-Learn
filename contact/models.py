from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.contrib.auth.models import User
from django.utils import timezone

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
    
    


class ContactPage(PageBase):
    description = models.TextField()



class Info(models.Model):
    place = models.CharField( max_length=50)
    phone_number = models.CharField( max_length=20)
    email = models.EmailField( max_length=50)

    

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email

