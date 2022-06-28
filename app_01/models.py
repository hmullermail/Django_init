from django import db
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models. Model):
    title = models.CharField(max_length=255)
    # null for db
    # blank for forms
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='author')
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Article'
        # verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title