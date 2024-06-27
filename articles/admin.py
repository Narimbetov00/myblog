from django.contrib import admin
from . import models
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = models.Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Videos)