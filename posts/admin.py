from django.contrib import admin

# Register your models here.

from .models import Author, Categories, Post, Comment, PostView

admin.site.register(Author)
admin.site.register(Categories)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
