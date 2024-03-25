from django.contrib import admin

from .models import Ebook, Review

@admin.register(Ebook)
class Ebook(admin.ModelAdmin):
    list_display = ('author', 'title')
    
@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ('review_author', 'ebook', 'rating')

