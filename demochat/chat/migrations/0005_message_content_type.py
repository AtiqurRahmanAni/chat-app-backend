# Generated by Django 4.2.7 on 2023-12-04 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_rename_thread_userthread'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='content_type',
            field=models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('voice', 'Voice')], default='text', max_length=20),
        ),
    ]