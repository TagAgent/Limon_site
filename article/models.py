from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Hashtag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

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
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    update_date = models.DateField(auto_now=True, verbose_name='дата обновления')
    read_time = models.PositiveSmallIntegerField(verbose_name='время для чтения', default=4)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'


class PublicationComment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='Публикация')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано в ')

