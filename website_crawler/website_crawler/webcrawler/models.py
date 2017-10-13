from __future__ import unicode_literals

from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=40)
    link = models.CharField(max_length=40)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)
    user_id = models.IntegerField()
    ups = models.CharField(max_length=50)
    downs = models.CharField(max_length=50)
    score = models.IntegerField()


class Discusses(models.Model):
    comment = models.CharField(max_length=50)
    news_id = models.IntegerField()
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=False)
    user_id = models.IntegerField()
    parent_id = models.IntegerField()