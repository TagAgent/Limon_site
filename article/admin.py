from django.contrib import admin
from article.models import Publication, Category, Hashtag


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']

