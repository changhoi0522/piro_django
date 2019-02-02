from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from django import forms

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().prefetch_related('tag_set', 'comment_set')
    paginate_by = 10


post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')

post_new = CreateView.as_view(model=Post, fields='__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))