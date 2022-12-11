from django.contrib import admin
from .models import AboutSchool, Contacts, Post, WidgetLinks
# Register your models here.

admin.site.register(Post)
admin.site.register(AboutSchool)
admin.site.register(Contacts)
admin.site.register(WidgetLinks)