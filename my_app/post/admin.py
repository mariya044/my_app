from django.contrib import admin
from post.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["first_name",]

admin.site.register(Post, PostModelAdmin)
