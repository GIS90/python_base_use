# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render
from models import Article, Column


def index(request):
    columns = Column.objects.all()
    return render(request, 'index.html', {'columns': columns})


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})


def article_detail(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    return render(request, 'news/article.html', {'article': article})
