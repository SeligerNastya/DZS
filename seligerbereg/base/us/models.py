from django.db import models

class Us(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_images = models.ImageField(upload_to="us1/%Y/%m/%d/", blank=True)

    class Meta:
        verbose_name = "Статью"
        verbose_name_plural = "О нас"

class Home(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название дома")
    images = models.ImageField(upload_to="home", blank=True, verbose_name="Изображение")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"



class Photo(models.Model):
    home = models.ForeignKey(Home,on_delete=models.CASCADE,  verbose_name="Дом")
    add_photo = models.ImageField(upload_to="home_images/add", blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"


class Attractions(models.Model):
    title = models.CharField(max_length=200, verbose_name="Достопримечательность")
    image = models.ImageField(upload_to="attractions", blank=True, verbose_name="Изображение")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

class Photo1(models.Model):
    attractions = models.ForeignKey(Attractions,on_delete=models.CASCADE,  verbose_name="Дом")
    add_photo = models.ImageField(upload_to="attractions_images/add", blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "изображение "
        verbose_name_plural = "изображения достопримечательности"