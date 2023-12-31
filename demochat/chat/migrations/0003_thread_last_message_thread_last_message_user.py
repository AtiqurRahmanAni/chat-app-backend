# Generated by Django 4.2.7 on 2023-12-03 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_remove_thread_participants_thread_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='last_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message', to='chat.message'),
        ),
        migrations.AddField(
            model_name='thread',
            name='last_message_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
