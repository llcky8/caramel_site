from django.db import models

class Case(models.Model):
    title = models.CharField("Название кейса", max_length=200)
    description = models.TextField("Описание кейса")
    image = models.ImageField("Изображение кейса", upload_to='cases_images/')
    tags = models.CharField("Теги", max_length=200)

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'
