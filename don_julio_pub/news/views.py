from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import NewsItem

# Create your views here.
def news_list(request: HttpRequest):
    return render(request, "news/news.html")