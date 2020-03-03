from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default='')
    comment = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default='')
    status = models.CharField(max_length=10, choices=[
                              ('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, verbose_name='Категория', null=True, blank=True)
    author = models.ForeignKey(
        User, null=True, default=None, on_delete=models.CASCADE)
