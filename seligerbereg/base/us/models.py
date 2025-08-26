from django.db import models

class Us(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_images = models.ImageField(upload_to="projects/%Y/%m/%d/", blank=True)

