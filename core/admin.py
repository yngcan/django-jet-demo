from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class MyUserAdmin(UserAdmin):
    list_per_page = 5
    date_hierarchy = 'date_joined'

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)