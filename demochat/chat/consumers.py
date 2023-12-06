import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import *


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # # Receive message from WebSocket
    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)

    #     message = text_data_json["message"]
    #     message_type = text_data_json["message_type"]
    #     message_owner = text_data_json["from"]

    #     # print(message, message_type, message_owner, self.room_name)
    #     msgObj = Message(user_id=message_owner, thread_id=self.room_name,
    #                      content=message, content_type=message_type)
    #     msgObj.save()

    #     # Send message to room group
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name, {"type": "chat.message",
    #                                "message": message, "message_type": message_type, "message_owner": message_owner},
    #     )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        message_type = event["message_type"]
        message_owner = event["message_owner"]
        upload = event["upload"]

        # Send message to WebSocket
        self.send(text_data=json.dumps(
            {"message": message, "message_type": message_type, "message_owner": message_owner, "upload": upload}))
