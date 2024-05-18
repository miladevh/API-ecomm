from rest_framework import serializers
from .models import User



class UserRegisterSerializer(serializers.ModelSerializer):
    
    vrfy_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'full_name', 'password', 'vrfy_password']
        extra_kwargs = {
            'password':{'write_only':True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('The email address is already in use')
        return value

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError('The phone number is already in use')
        return value
    
    def validate(self, data):
        if data['password'] != data['vrfy_password']:
            raise serializers.ValidationError('Passwords must match')
        return data
    
    def create(self, validated_data):
        del validated_data['vrfy_password']
        return User.objects.create_user(**validated_data,)




    