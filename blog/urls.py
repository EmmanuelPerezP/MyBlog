from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.BlogPostListView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)$', views.BlogPost.as_view(), name='post-detail'),
    url(r'^about/$', views.AboutMe.as_view(), name='about'),
    url(r'^contact/$', views.Contact.as_view(), name='contact'),
]
