from django.contrib import admin
from .models import Image, SocialMedia, UserInformation

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = "im"
    empty_value_display = "-пусто-"


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("name", "discription")
    empty_value_display = "-пусто-"


class UserInformationAdmin(admin.ModelAdmin):
    list_display = ("id", "socials")
    empty_value_display = "-пусто-"


admin.site.register(Image)
admin.site.register(SocialMedia)
admin.site.register(UserInformation)

