from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . models import *
from .serializers import *
from rest_framework import permissions


class UserThreadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = UserThread.objects.filter(participants=request.user)

        serializer = UserThreadSerializer(queryset, many=True)

        return Response({"data": serializer.data})


class UserMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        thread_id = request.query_params.get('thread_id')
        queryset = Message.objects.filter(thread_id=thread_id)

        serializer = MessageSerializer(queryset, many=True)
        return Response({"data": serializer.data})
