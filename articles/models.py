from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200,blank=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/',blank=True)
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail',args=[str(self.id)])
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.comment
    def get_absolute_url(self):
        return reverse('article_list')

class Videos(models.Model):
    title = models.CharField(max_length=150)
    Videos = models.FileField(upload_to='video/%y')