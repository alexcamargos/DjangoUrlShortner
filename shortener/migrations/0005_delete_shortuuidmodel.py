# Generated by Django 4.0.5 on 2022-07-05 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_rename_updated_at_uniformresourcelocator_edited_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShortUUIDModel',
        ),
    ]
