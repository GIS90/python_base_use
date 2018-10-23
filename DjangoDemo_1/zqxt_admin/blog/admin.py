from django.contrib import admin

# Register your models here.
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pubtime', 'updtime')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('fullname',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Article, ArticleAdmin)
