from django.contrib import admin
from .models import AboutSchool, News, Post
# Register your models here.

admin.site.register(News)
admin.site.register(Post)
admin.site.register(AboutSchool)