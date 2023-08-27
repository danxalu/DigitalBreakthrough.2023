from django.contrib import admin
from .models import Image

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = "im"
    empty_value_display = "-пусто-"


admin.site.register(Image)

