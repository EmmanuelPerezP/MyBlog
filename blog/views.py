# from django.shortcuts import render
from django.views import generic
from .models import Post, Tag, Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogPostListView(generic.ListView):
    model = Post
    context_object_name = 'blog_posts'
    template_name = 'index.html'
    paginate_by = 3


class BlogPost(generic.DetailView):
    model = Post
    # context_object_name = 'post'
    template_name = 'post.html'

class BlogPostCreate(generic.CreateView):
    model = Post
    fields = '__all__'

class BlogPostUpdate(generic.UpdateView):
    model = Post
    fields = '__all__'

class BlogPostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('/blog/')

class AboutMe(generic.TemplateView):
    template_name = 'about.html'


class Contact(generic.TemplateView):
    template_name = 'contact.html'
