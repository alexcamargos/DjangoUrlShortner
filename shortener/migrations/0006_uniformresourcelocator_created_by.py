# Generated by Django 4.0.5 on 2022-07-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_delete_shortuuidmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniformresourcelocator',
            name='created_by',
            field=models.CharField(default='', max_length=128),
        ),
    ]
