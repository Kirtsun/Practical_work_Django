from django.contrib import admin

from .models import Posts, Comments


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", )
    fieldsets = [
        (None, {'fields': ['text', 'author', 'title', 'create_date', 'published_date', 'is_publish']})]
    list_filter = ['title']
    search_fields = ['title']
    save_as = True


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("text", 'published_date', 'is_publish', 'post')
    fieldsets = [
        (None, {'fields': ['text', 'is_publish', 'post', 'published_date']})]
    list_filter = ['text']
    search_fields = ['text']
    save_as = True
