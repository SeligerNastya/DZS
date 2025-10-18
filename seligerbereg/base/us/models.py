from django.db import models

class Us(models.Model):
    title = models.CharField(max_length=200, verbose_name="название")
    featured_images = models.ImageField(upload_to="us_images/", blank=True, verbose_name="Изображение")
    description = models.TextField( blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статью"
        verbose_name_plural = "О нас"

class Photo(models.Model):
    us = models.ForeignKey(Us,on_delete=models.CASCADE,  verbose_name="О нас")
    add_photo = models.ImageField(upload_to="us_images/add/", blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"





class Home(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название дома")
    images = models.ImageField(upload_to="home_images/", blank=True, verbose_name="Изображение")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
    description = models.TextField( blank=True, verbose_name="Описание")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"



class Photo1(models.Model):
    home = models.ForeignKey(Home,on_delete=models.CASCADE,  verbose_name="Дом")
    add_photo = models.ImageField(upload_to="home_images/add/", blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"


class Attractions(models.Model):
    title = models.CharField(max_length=200, verbose_name="Достопримечательность")
    image = models.ImageField(upload_to="attractions_images/", blank=True, verbose_name="Изображение")
    description = models.TextField( blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

class Photo2(models.Model):
    attractions = models.ForeignKey(Attractions,on_delete=models.CASCADE,  verbose_name="Достопримечательность")
    add_photo = models.ImageField(upload_to="attractions_images/add/", blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "изображение "
        verbose_name_plural = "изображения достопримечательности"