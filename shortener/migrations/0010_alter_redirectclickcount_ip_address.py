# Generated by Django 4.0.5 on 2022-07-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0009_rename_uniformresourcelocatorclick_redirectclickcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirectclickcount',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
    ]
