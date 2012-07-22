__author__ = 'victor'

from blog.models import Post
from django.views.generic import ListView, DetailView
from django.conf.urls import patterns, include, url

urlpatterns=patterns('blog.views',
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-created")[:2],
                                    template_name="blog_template.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
                                    template_name='post_template.html')),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    )