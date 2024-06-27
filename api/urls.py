from django.urls import path
from . import views
urlpatterns=[
    path('',views.ArticleAPIView.as_view()),
    path('videos/',views.VideoAPIView.as_view()),
    
]