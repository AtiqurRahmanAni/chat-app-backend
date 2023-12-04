# Generated by Django 4.2.7 on 2023-12-03 13:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='participants',
        ),
        migrations.AddField(
            model_name='thread',
            name='participants',
            field=models.ManyToManyField(related_name='thread', to=settings.AUTH_USER_MODEL),
        ),
    ]
