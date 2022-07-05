from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

class ShortUUIDModel(models.Model):
    # A primary key ID of length 16 and a short alphabet.
    unique_identifier = ShortUUIDField(
        length=6,
        max_length=6,
        alphabet="abcdefABCDEF123456",
    )


class UniformResourceLocator(models.Model):
    # id = models.CharField(max_length=40, primary_key=True)
    url = models.URLField(max_length=10_000)
    uuid = models.CharField(max_length=8)
    short_url = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
