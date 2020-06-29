from django.contrib import admin
from blog.models import Category,Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Category)

class PostAdmin(SummernoteModelAdmin):
    summernote_field=('content',)

admin.site.register(Post,PostAdmin)