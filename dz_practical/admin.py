from django.contrib import admin

from .models import Comments, Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", 'text', 'published_date', 'is_publish', 'create_date', 'author')
    fieldsets = [
        (None, {'fields': ['text', 'author', 'title', 'create_date', 'published_date', 'is_publish']})]
    list_filter = ['create_date']
    search_fields = ['title']
    date_hierarchy = 'published_date'
    save_as = True


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("text", 'published_date', 'is_publish', 'post')
    fieldsets = [
        (None, {'fields': ['text', 'is_publish', 'post', 'published_date', 'name']})]
    list_filter = ['published_date']
    date_hierarchy = 'published_date'
    search_fields = ['text']
    save_as = True
