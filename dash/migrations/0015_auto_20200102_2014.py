# Generated by Django 3.0 on 2020-01-02 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0014_lesson_instructions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='instructions',
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.Lesson')),
            ],
        ),
    ]
