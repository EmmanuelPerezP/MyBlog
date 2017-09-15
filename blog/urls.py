from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.BlogPostListView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)$', views.BlogPost.as_view(), name='post-detail'),
    url(r'^acerca/$', views.AboutMe.as_view(), name='about'),
    url(r'^contacto/$', views.Contact.as_view(), name='contact'),
    url(r'^new-post/$', views.Contact.as_view(), name='newPost'),
]

urlpatterns += [
    url(r'^post/create/$', views.BlogPostCreate.as_view(), name='post_create'),
    url(r'^post/(?P<pk>\d+)/update/$', views.BlogPostUpdate.as_view(),
        name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.BlogPostDelete.as_view(),
        name='post_delete'),
]
