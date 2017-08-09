from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.BlogPostListView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)$', views.BlogPost.as_view(), name='post-detail'),
    url(r'^about/$', views.AboutMe.as_view(), name='about'),
    url(r'^contact/$', views.Contact.as_view(), name='contact'),
    url(r'^new-post/$', views.Contact.as_view(), name='newPost'),
]
