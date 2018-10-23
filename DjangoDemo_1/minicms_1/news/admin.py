# coding: utf-8

from django.contrib import admin
from .models import Column, Article
# Register your models here.


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_time', 'update_time')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)
