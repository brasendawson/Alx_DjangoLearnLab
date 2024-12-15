from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    permissions.IsAuthenticated
    CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.followers.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}"})

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    permissions.IsAuthenticated
    CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.followers.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"})


# Create your views here.
