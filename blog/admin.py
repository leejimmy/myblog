from django.contrib import admin

# Register your models here.
from .models import Category,Blog,Tag


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','created')

admin.site.register([Tag,Category])
admin.site.register(Blog,BlogAdmin)