from django.contrib import admin
from .models import Photo

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "caption")

admin.site.register(Photo ,PostAdmin)
