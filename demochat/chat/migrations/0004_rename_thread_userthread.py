# Generated by Django 4.2.7 on 2023-12-03 13:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_thread_last_message_thread_last_message_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thread',
            new_name='UserThread',
        ),
    ]
