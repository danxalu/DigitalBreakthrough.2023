from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Image(models.Model):
    im = models.FileField(verbose_name="Скриншот")


class SocialMedia(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название социальной сети")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name


class UserInformation(models.Model):
    id_in_socials = models.TextField(verbose_name="Никнейм")
    socials = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, related_name="posts", blank=True, null=True,
                                verbose_name="Медиа")
