import nested_admin
from django.contrib import admin
from .models import Article, Comment, Attachment, StatusEmot


class EmotInline(nested_admin.NestedTabularInline):
    model = StatusEmot

class AttachmentInline(nested_admin.NestedTabularInline):
    model = Attachment
    extra = 0
    inlines = [EmotInline]


class CommentInline(nested_admin.NestedStackedInline):
    model = Comment
    inlines = [AttachmentInline]
    extra = 0


@admin.register(Article)
class ArticleAdmin(nested_admin.NestedModelAdmin):
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
