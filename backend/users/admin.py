from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_musician', 'is_studio_owner')