from django.shortcuts import render
from rest_framework.generics import ListAPIView
from articles.models import Article,Videos
from .serializers import ArticleSerializer,VideoSerializer

# Create your views here.

class ArticleAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class VideoAPIView(ListAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer