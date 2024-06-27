from rest_framework import serializers

from articles.models import Article,Videos

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','summary','body','photo','data','author')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('title','Videos')
