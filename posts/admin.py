from django.contrib import admin
from .models import Posts

@admin.register(Posts)
class Post(admin.ModelAdmin):
    list_display = ('id', 'user')