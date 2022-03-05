from re import search
from django.contrib import admin
from matplotlib.font_manager import list_fonts

from . models import *

# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name']

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title','slug','description','image']
    search_fields = ('title','cat_id')

