from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Post
from django import forms


post_list = ListView.as_view(model=Post, paginate_by=5)

post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')

post_new = CreateView.as_view(model=Post, fields='__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')