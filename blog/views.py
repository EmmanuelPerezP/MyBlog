# from django.shortcuts import render
from django.views import generic
from .models import Post, Tag, Category


class BlogPostListView(generic.ListView):
    model = Post
    context_object_name = 'blog_posts'
    template_name = 'index.html'


class BlogPost(generic.DetailView):
    model = Post
    # context_object_name = 'post'
    template_name = 'post.html'
