from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . models import *
from .serializers import *
from rest_framework import permissions
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from enum import Enum

channel_layer = get_channel_layer()


class MessageTypes(Enum):
    Text = "text"
    Image = "image"
    Voice = "voice"


class UserThreadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = UserThread.objects.filter(participants=request.user)

        serializer = UserThreadSerializer(
            queryset, many=True)

        return Response({"data": serializer.data})


class UserMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        thread_id = request.query_params.get('thread_id')
        queryset = Message.objects.filter(thread_id=thread_id)

        serializer = MessageSerializer(
            queryset, many=True, context={"request": request})
        return Response({"data": serializer.data})

    def post(self, request, format=None):
        user_id = int(request.data.get('user_id'))
        thread_id = int(request.data.get('thread_id'))
        message = request.data.get('message')
        message_type = request.data.get('message_type')
        message_files = request.FILES.get('message_files')

        # print(user_id, thread_id, message, message_type, message_files)
        try:

            msgObj = Message(user_id=user_id, thread_id=thread_id,
                             content=message, content_type=message_type, upload=message_files)
            msgObj.save()

            upload = None
            if message_type == MessageTypes.Image.value:
                upload = request.build_absolute_uri(
                    msgObj.upload.url)

            async_to_sync(channel_layer.group_send)(f"chat_{thread_id}", {"type": "chat.message",
                                                                          "message": message, "message_type": message_type, "message_owner": user_id, "upload": upload})

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            print(e)
            return Response({"detail": "Something went wrong sending message"}, status=status.HTTP_400_BAD_REQUEST)
