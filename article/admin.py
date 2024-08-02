from django.contrib import admin
from article.models import Publication, PublicationComment, Category, Hashtag


@admin.register(PublicationComment)
class PublicationCommentAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']

