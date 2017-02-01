"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField(max_length=1000)

class Track(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

class Session(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.TextField(max_length=1000)
    track = models.ForeignKey(Track)
    speaker = models.ForeignKey(Speaker)
