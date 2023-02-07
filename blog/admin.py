from django.contrib import admin
from .models import Post, Author, Tag, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author")
    list_filter = ("date", "author", "tags")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "post",)
    list_filter = ("post",)
    search_fields = ("user_name", "user_email", "text")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
