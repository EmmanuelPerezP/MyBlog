# from django.shortcuts import render
from django.views import generic
from .models import Post, Tag, Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class BlogPostListView(generic.ListView):
    model = Post
    context_object_name = 'blog_posts'
    template_name = 'index.html'
    paginate_by = 3


class BlogPost(generic.DetailView):

    model = Post
    # context_object_name = 'post'
    template_name = 'post.html'


class BlogPostCreate(LoginRequiredMixin, PermissionRequiredMixin,
                     generic.CreateView):
    permission_required = 'blog.is_staff'
    model = Post
    fields = '__all__'


class BlogPostUpdate(LoginRequiredMixin, PermissionRequiredMixin,
                     generic.UpdateView):
    permission_required = 'blog.is_staff'
    model = Post
    fields = '__all__'


class BlogPostDelete(LoginRequiredMixin, PermissionRequiredMixin,
                     generic.DeleteView):
    permission_required = 'blog.is_staff'
    model = Post
    success_url = reverse_lazy('index')


class AboutMe(generic.TemplateView):
    template_name = 'about.html'


class Contact(generic.TemplateView):
    template_name = 'contact.html'
