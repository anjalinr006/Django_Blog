from django.contrib import admin

from .models import Post
from django_summernote.admin import SummernoteModelAdmin

class PostModelAdmin(SummernoteModelAdmin):
    list_display = ["title","timesstamp"]
    list_filter = ["timesstamp"]
    search_fields = ["content", "title"]
    summernote_fields = '__all__'
    class Meta:
        model = Post

admin.site.register(Post,PostModelAdmin)

