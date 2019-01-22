#blog/admin.py

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content']

admin.site.register(Post, PostAdmin) # 참고: 같은 모델 중복 등록은 불가
