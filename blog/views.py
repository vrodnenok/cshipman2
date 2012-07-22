# Create your views here.
from django.shortcuts import render_to_response
from blog.models import Post

def home(request):
    posts=Post.objects.all()
    return render_to_response('blog_template.html')

def tagpage(request, tag):
    posts=Post.objects.filter(tags__name=tag)
    return render_to_response('tagpage_template.html', {'posts':posts, 'tag':tag})
