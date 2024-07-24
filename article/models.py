from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    creation_date = models.DateField()
