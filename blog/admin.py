#blog/admin.py

from django.contrib import admin
from .models import Post, Tag
from .models import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','content_size', 'status', 'content']

    actions = ['make_published','make_draft',]

    def content_size(self, post):
        return '{}'.format(len(post.content))
    content_size.short_description = '글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published 상태로 변경합니다.'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft 상태로 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 Draft 상태로 변경합니다.'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
