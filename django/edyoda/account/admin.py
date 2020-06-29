from django.contrib import admin
# from user.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(get_user_model(),UserAdmin)


# class UserAdmin(SummernoteModelAdmin):
#     summernote_field=('bio',)

# admin.site.register(get_user_model(),UserAdmin)