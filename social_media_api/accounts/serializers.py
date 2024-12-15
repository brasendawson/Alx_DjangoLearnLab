from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User  = get_user_model()
serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        get_user_model().objects.create_user
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        user.set_password(validated_data['password'])  
        user.save() 
        Token.objects.create(user=user)  
        return user