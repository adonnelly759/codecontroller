# Generated by Django 3.0 on 2020-02-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0019_auto_20200206_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonprogress',
            name='code',
        ),
        migrations.AlterField(
            model_name='lessonprogress',
            name='finish',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
