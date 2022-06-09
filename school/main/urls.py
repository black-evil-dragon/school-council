from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView


urlpatterns = [
    path('', views.index),
    path('school/about', views.about),
    path('news', views.news),
    path('menu', views.menu),
    path('ghost', views.ghost),

    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='news'),
]

