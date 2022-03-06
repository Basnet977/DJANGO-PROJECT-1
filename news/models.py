from distutils.command import upload
from tkinter import TRUE
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.cat_name

class Blog(models.Model):
    cat_id = models.ForeignKey(Category,on_delete=models.PROTECT)
    title = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255,unique=True)
    image = models.ImageField(upload_to = 'Blog',blank=True,null=True)
    description = RichTextField()



class Demo(models.Model):
    name = models.CharField(max_length=255)
