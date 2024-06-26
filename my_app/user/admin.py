from django.contrib import admin
from django.contrib import admin
from user.models import MyUser


class MyUserModelAdmin(admin.ModelAdmin):
    list_display = ["email",]

admin.site.register(MyUser, MyUserModelAdmin)
