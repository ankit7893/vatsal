from django.contrib import admin

from .models import Image

# admin.site.register(Image)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['photo' , 'date']





