from django.contrib import admin
from .models import movie
# Register your models here.

class movieadmin(admin.ModelAdmin):
    list_display=['MovieName','Timing','Location']

admin.site.register(movie,movieadmin)
