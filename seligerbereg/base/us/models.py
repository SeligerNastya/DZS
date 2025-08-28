from django.db import models

class Us(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_images = models.ImageField(upload_to="us1/%Y/%m/%d/", blank=True)

class Home(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(blank=True)
    featured_images = models.ImageField(upload_to="home/%Y/%m/%d/", blank=True)