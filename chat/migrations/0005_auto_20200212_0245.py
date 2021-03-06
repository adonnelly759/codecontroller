# Generated by Django 3.0 on 2020-02-12 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_message_roomname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='roomName',
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chat.Room'),
        ),
    ]
