# from django.shortcuts import render
from django.views import generic
from .models import Post, Tag, Category


class BlogPostListView(generic.ListView):
    model = Post
    context_object_name = 'blog_posts'
    template_name = 'index.html'
    paginate_by = 3


class BlogPost(generic.DetailView):
    model = Post
    # context_object_name = 'post'
    template_name = 'post.html'


class AboutMe(generic.TemplateView):
    template_name = 'about.html'


class Contact(generic.TemplateView):
    template_name = 'contact.html'
