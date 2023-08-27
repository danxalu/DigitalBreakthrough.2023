from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Image(models.Model):
    im = models.FileField(verbose_name="Скриншот")
