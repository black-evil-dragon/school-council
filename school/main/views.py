from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import AboutSchool, Contacts, Post, WidgetLinks


def index(request):
    news = Post.objects.order_by('-id')[:3]
    contacts = Contacts.objects.order_by('-id')[:1]
    return render(request, 'main/pages/index.html', {'post': news, 'contacts': contacts})

def about(request):
    aboutContent = AboutSchool.objects.order_by('id')
    return render(request, 'main/pages/about.html', {'about': aboutContent})

def news(request):
    post = Post.objects.order_by('-id')
    widgets = WidgetLinks.objects.order_by('id')
    return render(request, 'main/pages/news.html', {'post': post, 'widgets': widgets})

def ghost(request):
    return render(request, 'main/pages/ghost.html')

def council(request):
    return render(request, 'main/pages/council.html')

def widget(request, link):
    if link != 'ghost':
        return render(request, f'main/pages/articles/{link}.html')
    else:
        return render(request, f'main/pages/ghost.html')

def reach(request):
    return render(request, f'main/pages/reach.html')




class BlogListView(ListView):
    model = Post
    template_name = 'main/pages/news.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'main/pages/post.html'


