# Generated by Django 3.0 on 2020-01-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0013_auto_20200101_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='instructions',
            field=models.TextField(default=''),
        ),
    ]
