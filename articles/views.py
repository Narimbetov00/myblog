from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
# Create your views here.
from . import models

class ArticlaListView(ListView):
    model = models.Article
    template_name = 'article_list.html'

def VideosView(request):
    videos = models.Videos.objects.all()
    return render(request,'post_video.html',{'videos':videos})

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.Article
    fields = ('title','summary','body','photo')
    template_name = 'article_edit.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author== self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    
    def test_func(self):
        obj = self.get_object()
        return obj.author== self.request.user
class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ('title','summary','body','photo',)

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self) -> bool | None:
        return self.request.user.is_superuser