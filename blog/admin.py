from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'author']
    list_filter = ('status', 'created_on')
    summernote_fields = ('ingredients', 'instructions')


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'recipe', 'created_on')
    list_filter = ('created_on', 'name')
    search_fields = ('body', 'name')