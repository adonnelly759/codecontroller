# Generated by Django 3.0 on 2020-02-17 16:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0020_auto_20200209_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
