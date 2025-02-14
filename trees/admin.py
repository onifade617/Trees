from django.contrib import admin

# Register your models here.
from .models import Tree

class TreeAdmin(admin.ModelAdmin):
    list_display = ("title", "farmer", "price",)

admin.site.register(Tree, TreeAdmin)