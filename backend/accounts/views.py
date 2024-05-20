from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (UserRegisterSerializer, UserChangePasswordSerializer, 
                          UserProfileSerializer, ProfileSerializer)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserProfile
from django.shortcuts import get_object_or_404


class UserRegister(APIView):

    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePassword(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        ser_data = UserChangePasswordSerializer(data=request.POST, )
        if ser_data.is_valid():
            ser_data.update(user, ser_data.validated_data)
            return Response(ser_data.data)
        


class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # profile = get_object_or_404(UserProfile, user=request.user)
        user = request.user
        serializer = UserProfileSerializer(instance=user,)
        return Response(serializer.data)
    

class UserProfileChange(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user.profile
        ser_data = ProfileSerializer(instance=user, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,)

        












