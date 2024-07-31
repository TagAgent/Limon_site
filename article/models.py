from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Hashtag(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Хэштэги'
        verbose_name = 'Хэштэг'


class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='publications', verbose_name='Категория', null=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='publiucations', verbose_name='Хэштеги', null=True)

    name = models.CharField(max_length=50, verbose_name='название')
    short_description = models.CharField(max_length=200, verbose_name='краткое содержание')
    description = models.TextField(verbose_name='полное содержание')
    image = models.ImageField(verbose_name='изображение')
    creation_date = models.DateField(verbose_name='дата создания')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'
