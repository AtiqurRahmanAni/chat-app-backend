from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . models import User
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from rest_framework import permissions


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if user:
            raise AuthenticationFailed(detail="User already registered")

        new_user = User.objects.create(email=email)
        new_user.set_password(password)
        new_user.save()

        return Response(status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed(detail="No user with email")

        if not user.check_password(password):
            raise AuthenticationFailed(detail="Incorrect password")

        serializer = UserWithTokensSerializer(user)

        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class UserView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        serializer = UserSerializer(user)

        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class TestTokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({'data': "Ok"}, status=status.HTTP_200_OK)


class LogoutView(APIView):

    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
