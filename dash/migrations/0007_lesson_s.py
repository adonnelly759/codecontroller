# Generated by Django 3.0 on 2020-01-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0006_auto_20191221_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='s',
            field=models.SlugField(default='def', unique=True),
            preserve_default=False,
        ),
    ]
