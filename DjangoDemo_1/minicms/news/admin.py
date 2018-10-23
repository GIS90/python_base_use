# coding: utf-8

from django.contrib import admin
from .models import Article, Column


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_time', 'update_time')


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)
