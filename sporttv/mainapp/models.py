from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Slider(models.Model):
    image = models.FileField(upload_to='images',blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    sub_title = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title


STATUS=(
    ('publish','publish'),
    ('unpublish','unpublish'),
)
class News(models.Model):
    news_title = models.CharField(max_length=200,blank=True,null=True,default=None)
    description = RichTextField()
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=200,choices=STATUS)

    def __str__(self):
        return self.news_title


class Email(models.Model):
    email_title = models.CharField(max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return self.email_title


class Contact(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    website = models.CharField(max_length=200,null=True,blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    image = models.FileField(upload_to='images',blank=True,null=True)
    status = models.CharField(max_length=200,choices=STATUS,default='unpublish')

    def __str__(self):
        return self.title


class About(models.Model):
    description = RichTextField()

    def __str__(self):
        return self.description