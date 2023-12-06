from django.db import models
from authentication.models import User
from uuid import uuid4
import os


def message_file_path(instance, filename):
    _, ext = os.path.splitext(filename)
    return f"message_files/{uuid4().hex + ext}"


class UserThread(models.Model):
    participants = models.ManyToManyField(User, related_name='thread')
    last_message = models.ForeignKey(
        'Message', on_delete=models.SET_NULL, null=True, blank=True, related_name='message')
    last_message_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='message_user')


class Message(models.Model):
    class ContentTypes(models.TextChoices):
        TEXT = "text"
        IMAGE = "image"
        VOICE = "voice"

    thread = models.ForeignKey(UserThread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    content_type = models.CharField(
        max_length=20, choices=ContentTypes.choices, default=ContentTypes.TEXT)
    upload = models.FileField(upload_to=message_file_path, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.thread.last_message = self
        self.thread.last_message_user = self.user
        self.thread.save()
