from django.db import models

class Dz(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='dz/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title