from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from django import forms


post_list = ListView.as_view(model=Post, paginate_by=5)

post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')

post_new = CreateView.as_view(model=Post, fields='__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))