from django.urls import path 
from . import views

urlpatterns = [
    path('<int:pk>/edit/',views.ArticleUpdateView.as_view(),name='article_edit'),
    path('<int:pk>/',views.ArticleDetailView.as_view(),name='article_detail'),
    path('<int:pk>/delete/',views.ArticleDeleteView.as_view(),name='article_delete'),
    path('new/',views.ArticleCreateView.as_view(),name='article_new'),
    path('videos/',views.VideosView,name='post_video'),
    path('',views.ArticlaListView.as_view(),name='article_list'),
]