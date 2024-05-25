from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (UserRegisterSerializer, UserChangePasswordSerializer, 
                          UserProfileSerializer, ProfileSerializer)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema, OpenApiResponse


class UserRegister(APIView):
    # Documentation
    """
    description: register new user
    url: /register/
    """
    @extend_schema(
        description="register new user",
        request=UserRegisterSerializer,
        responses={
            201: OpenApiResponse(
                response=UserRegisterSerializer,
                description="user created"
            ),
            400: OpenApiResponse(
                response={"message": 'bad_request'},
                description="bad request"
            )
        }
    )
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePassword(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Documentation
    """
    description: Password changed successfully
    url: /change_password/
    """
    @extend_schema(
        description="user change password",
        request=UserChangePasswordSerializer,
        responses={
            202: OpenApiResponse(
                response=UserChangePasswordSerializer,
                description="Password changed successfully"
            )
        }
    )
    def post(self, request):
        user = request.user
        ser_data = UserChangePasswordSerializer(data=request.POST, )
        if ser_data.is_valid():
            ser_data.update(user, ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)
        


class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Documenation
    """
    description: show user profile
    url: /user_profile/
    """
    @extend_schema(
        description="show user profile",
        responses={
            200: OpenApiResponse(
                response=UserProfileSerializer,
                description="profile"
            )
        }
    )
    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(instance=user,)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserProfileChange(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Documenation
    """
    description: change user profile
    url: /change_profile/
    """
    @extend_schema(
        description="change user profile",
        request=ProfileSerializer,
        responses={
            202: OpenApiResponse(
                response=ProfileSerializer,
                description="Information changed successfully"
            )
        }
    )
    def put(self, request):
        user = request.user.profile
        ser_data = ProfileSerializer(instance=user, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)

        












