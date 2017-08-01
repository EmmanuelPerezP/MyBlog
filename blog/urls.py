from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.BlogPostListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', views.BlogPost.as_view(), name='post-detail'),
]
