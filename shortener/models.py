from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

class UniformResourceLocator(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=10_000)
    alias = ShortUUIDField(length=6, max_length=6, alphabet="abcdefABCDEF123456", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.alias} -> {self.url}'
    
    def get_date_created(self):
        return str(self.created_at)
    
    def get_date_created_human_friendly(self):
        return self.created_at.strftime("%d %b %Y %H:%M:%S")
    
    def get_date_edited(self):
        return str(self.edited_at)

    def get_date_edited_human_friendly(self):
        return self.edited.strftime("%d %b %Y %H:%M:%S")
    
    def get_alias(self):
        return self.alias
    
    def get_url(self):
        return self.url
