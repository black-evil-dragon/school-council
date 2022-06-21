from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import News, Post
from .forms import NewsForm


def index(request):
    news = Post.objects.order_by('-id')[:1]
    return render(request, 'main/index.html', {'post': news})

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/school/about.html')

def news(request):
    post = Post.objects.order_by('-id')
    return render(request, 'main/news.html', {'post': post})

def menu(request):
    return render(request, 'main/menu.html')

def ghost(request):
    return render(request, 'main/ghost.html')




class BlogListView(ListView):
    model = Post
    template_name = 'main/news.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'main/post.html'


