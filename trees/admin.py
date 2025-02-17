from django.contrib import admin

# Register your models here.
from .models import Tree, Review

class ReviewInline(admin.TabularInline):
    model = Review

class TreeAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    
    list_display = ("title", "farmer", "price",)

admin.site.register(Tree, TreeAdmin)