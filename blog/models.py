# blog/models.py

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목', help_text='제목을 입력해주세요. 최대 100자')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

