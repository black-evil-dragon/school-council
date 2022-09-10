from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import AboutSchool, News, Post
from .forms import NewsForm


def index(request):
    news = Post.objects.order_by('-id')[:1]
    return render(request, 'main/pages/index.html', {'post': news})

def about(request):
    aboutContent = AboutSchool.objects.order_by('id')
    return render(request, 'main/pages/about.html', {'about': aboutContent})

def news(request):
    post = Post.objects.order_by('-id')
    return render(request, 'main/pages/news.html', {'post': post})

def menu(request):
    return render(request, 'main/menu.html')

def ghost(request):
    return render(request, 'main/pages/ghost.html')




class BlogListView(ListView):
    model = Post
    template_name = 'main/pages/news.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'main/pages/post.html'


