from django.views.generic import ListView, CreateView
from .models import Post
from django import forms


post_list = ListView.as_view(model=Post, paginate_by=5)


#blog/forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
##############
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = ''g