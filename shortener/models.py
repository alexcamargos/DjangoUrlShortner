from ipaddress import ip_address
from django.db import models

from shortuuid.django_fields import ShortUUIDField


# Create your models here.

class UniformResourceLocator(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=10_000)
    alias = ShortUUIDField(length=6, max_length=6, alphabet="abcdefABCDEF123456", unique=True)
    created_by = models.CharField(max_length=128, default="")
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
    
    def get_total_clicks(self):
        clicks = RedirectClickCount.objects.filter(link=self)
        total_clicks = clicks.aggregate(total_clicks=models.Sum('clicks_count'))['total_clicks']

        return 0 if total_clicks is None else total_clicks


class RedirectClickCount(models.Model):
    link = models.ForeignKey(to=UniformResourceLocator, on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    clicks_count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.link.alias} -> {self.clicks_count}'
