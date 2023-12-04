from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . models import *


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class UserThreadSerializer(ModelSerializer):
    last_message_user = serializers.SerializerMethodField()
    last_message_content = serializers.SerializerMethodField()
    participants_emails = serializers.SerializerMethodField()

    class Meta:
        model = UserThread
        fields = ['id', 'participants_emails',
                  'last_message_content', 'last_message_user']

    def get_last_message_user(self, obj):
        return obj.last_message_user.email if obj.last_message_user else None

    def get_last_message_content(self, obj):
        return obj.last_message.content if obj.last_message.content else None

    def get_participants_emails(self, obj):
        return [participant.email for participant in obj.participants.all()] if obj.participants.exists() else []
