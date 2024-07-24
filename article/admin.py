from django.contrib import admin
from article.models import Publication


@admin.register(Publication)
class Publications(admin.ModelAdmin):
    pass
