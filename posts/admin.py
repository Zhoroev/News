from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    field = ['title', 'body']


admin.site.register(Post, PostAdmin)
